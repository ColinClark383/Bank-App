import { useState } from "react";
import { apiRequest } from "../api/client";

export default function CreateUser({ onBack }) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    try {
      await apiRequest("/api/customers", "POST", {
        name,
        email
      });

      alert("Customer created successfully");
      onBack();
    } catch (err) {
      alert(err.message);
    }
  }

  return (
    <div style={styles.container}>
      <form onSubmit={handleSubmit} style={styles.form}>
        <h2>Create Customer</h2>

        <input
          type="text"
          placeholder="Customer Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <button type="submit">Create Customer</button>

        <button type="button" onClick={onBack}>
          Back to Login
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