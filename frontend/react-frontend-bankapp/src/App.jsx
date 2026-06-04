import { useState } from "react";
import Navbar from "./components/Navbar";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import CreateUser from "./pages/CreateUser";
import { apiRequest } from "./api/client";

export default function App() {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);
  const [showCreateUser, setShowCreateUser] = useState(false);
  const [accountRefresh, setAccountRefresh] = useState(0);

  function handleLogin(userData, authToken) {
    setUser(userData);
    setToken(authToken);
  }

  function handleLogout() {
    setUser(null);
    setToken(null);
  }

  async function handleCreateAccount() {
    const accountType = prompt(
      "Enter account type (Checking, Savings, etc.)"
    );

    if (!accountType) return;

    const balanceInput = prompt(
      "Enter starting balance"
    );

    if (balanceInput === null) return;

    const balance = Number(balanceInput);

    if (isNaN(balance)) {
      alert("Invalid balance");
      return;
    }

    try {
      await apiRequest(
        "/api/accounts",
        "POST",
        {
          customer_id: token,
          account_type: accountType,
          balance: balance,
        }
      );

      alert("Account created");

      setAccountRefresh(prev => prev + 1);

    } catch (err) {
      alert(err.message);
    }
  }

  async function handleDeleteUser() {
    const confirmed = window.confirm(
      "Delete this customer and all associated accounts?"
    );

    if (!confirmed) return;

    try {
      await apiRequest(
        `/api/customers/${token}`,
        "DELETE"
      );

      alert("Customer deleted");

      handleLogout();
    } catch (err) {
      alert(err.message);
    }
  }

  return (
    <>
  <Navbar
  user={user}
  onLogout={handleLogout}
  onCreateAccount={handleCreateAccount}
  onDeleteUser={handleDeleteUser}
/>

  {!user ? (
    showCreateUser ? (
      <CreateUser
        onBack={() => setShowCreateUser(false)}
      />
    ) : (
      <Login
        onLogin={handleLogin}
        onCreateUser={() => setShowCreateUser(true)}
      />
    )
  ) : (
    <Dashboard
      user={user}
      token={token}
      accountRefresh={accountRefresh}
    />
  )}
</>
  );
}