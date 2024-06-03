#!/bin/bash

####### /bin/bash start.sh

apply_migrations() {
    echo "Applying migrations..."
    (cd  './investor_bulletin' && alembic upgrade head)
}

downgrade_migrations() {
    echo "Downgrading migrations..."
    (cd  './investor_bulletin' && alembic downgrade -1)
}

generate_migrations() {
    if [ $# -eq 0 ]; then
        echo "No message provided for running the command."
    else
        message="$1"
        if [ -z "$message" ]; then
            echo "Something wrong with the message '$message'."
        else
            echo "Generating migration $message..."
            (cd  './investor_bulletin' && alembic revision --autogenerate -m "$message")
        fi
    fi
}

run_app() {
    echo "running the docker compose up and its dependencies"
    (cd '..' && make up)
}

run_tests() {
    echo "running tests"
    pytest --cov=investor_bulletin
}

turn_off_app() {
    echo "running the docker compose down and its dependencies"
    (cd '..' && make down)
}

run_subscriber() {
    echo "running subscriber..."
    python investor_bulletin/event_subscriber/main.py
}

seed_data() {
    apply_migrations
    echo "seed_data: "
    (cd  './investor_bulletin/utils' && python data_seeder.py)
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Display menu if the script is run directly
    echo "Select an option:"
    echo "1. Apply migrations"
    echo "2. Generate migrations (with arguments)"
    echo "3. Downgrading migrations"
    echo "4. Seed data"
    echo "5. RUN APPLICATION..."
    echo "6. Turn off APPLICATION..."
    echo "7. Run tests"
    echo "8. Run event subscriber"

    # Read user input
    read -p "Enter your choice (1-8): " choice

    # Process user choice
    case $choice in
        1)
            apply_migrations
            ;;
        2)
            read -p "Enter the migration message: " message
            generate_migrations "$message"
            ;;
        3)
            downgrade_migrations
            ;;
        4)
            seed_data
            ;;
        5)
            run_app
            ;;
        6)
            turn_off_app
            ;;
        7)
            run_tests
            ;;
        8)
            run_subscriber
            ;;
        *)
            echo "Invalid choice. Please select a valid option '(1-8)'."
            ;;
    esac
fi
