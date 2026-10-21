def prog46():
    role = input("Enter role (admin/user/guest): ").strip().lower()
    match role:
        case "admin":
            print("Admin: Full access (read, write, delete, manage users)")
        case "user":
            print("User: Limited access (read, write)")
        case "guest":
            print("Guest: View-only access")
        case _:
            print("Unknown role: No access")

prog46()