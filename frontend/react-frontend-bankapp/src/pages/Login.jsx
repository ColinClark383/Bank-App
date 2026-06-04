import { useState } from "react";
import { apiRequest } from "../api/client";


export default function Login({ onLogin, onCreateUser }) {
  const [name, setName] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    try {
      const loginResponse = await apiRequest("/api/customers/search?name=" + name, "GET");
      const user = loginResponse[0]
      onLogin(user.name, user._id);
    } catch (err) {
      alert(err.message);
    }
  }

  return (
    <div style={styles.container}>
      <form onSubmit={handleSubmit} style={styles.form}>
        <h2>Bank Login</h2>

        <input
          type="text"
          placeholder="Customer Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <button type="submit">Login</button>

        <button
        type="button"
        onClick={onCreateUser}
        >
        Create New Customer
        </button>
      </form>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "12px",
    width: "300px",
  },
};