import json
from typing import Any


def load_users(filepath: str = "users.json") -> list[dict[str, Any]]:
    """Loads the list of users from a JSON file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filepath}'.")
        return []


def filter_users_by_name(users: list[dict[str, Any]], name: str) -> list[dict[str, Any]]:
    """Filters users by name (case-insensitive)."""
    return [
        user for user in users
        if user.get("name", "").lower() == name.lower()
    ]


def filter_users_by_age(users: list[dict[str, Any]], age: int) -> list[dict[str, Any]]:
    """Filters users by exact age."""
    return [user for user in users if user.get("age") == age]


def filter_users_by_email(users: list[dict[str, Any]], email: str) -> list[dict[str, Any]]:
    """Filters users by email address (case-insensitive)."""
    return [
        user for user in users
        if user.get("email", "").lower() == email.lower()
    ]


def display_users(users: list[dict[str, Any]]) -> None:
    """Prints a list of users to the console."""
    if not users:
        print("No matching users found.")
        return

    for user in users:
        print(user)


def main() -> None:
    """Main entry point for the user filtering CLI."""
    users = load_users()
    if not users:
        return

    filter_option = input(
        "What would you like to filter by? (name, age, email): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        results = filter_users_by_name(users, name_to_search)
        display_users(results)

    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            results = filter_users_by_age(users, age_to_search)
            display_users(results)
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        results = filter_users_by_email(users, email_to_search)
        display_users(results)

    else:
        print("Filtering by that option is not supported.")


if __name__ == "__main__":
    main()
