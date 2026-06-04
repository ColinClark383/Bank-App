export default function Navbar({
  user,
  onLogout,
  onCreateAccount,
  onDeleteUser,
}) {
  return (
    <nav style={styles.nav}>
      <h2>MyBank</h2>

      <div style={styles.right}>
        {user && (
          <>
            <span>Welcome, {user}</span>

            <button onClick={onCreateAccount}>
              New Account
            </button>

            <button onClick={onDeleteUser}>
              Delete Customer
            </button>

            <button onClick={onLogout}>
              Logout
            </button>
          </>
        )}
      </div>
    </nav>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    padding: "12px 20px",
    background: "#0f172a",
    color: "white",
  },
  right: {
    display: "flex",
    gap: "10px",
    alignItems: "center",
  },
};