import { useEffect, useState } from "react";
import { apiRequest } from "../api/client";
import AccountCard from "../components/AccountCard";

export default function Dashboard({ user, token, accountRefresh }) {
  const [accounts, setAccounts] = useState([]);
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    async function loadData() {
      const acc = await apiRequest("/api/accounts/search?id=" + token, "GET");

      setAccounts(acc);
    }

    loadData();
  }, [token]);

  useEffect(() => {
  loadAccounts();
}, [token]);

useEffect(() => {
    loadAccounts();
    }, [token, accountRefresh]);

async function loadAccounts() {
  const acc = await apiRequest("/api/accounts/search?id=" + token, "GET");
  setAccounts(acc);
}

  async function handleDeleteAccount(accountId) {
  const confirmed = window.confirm(
    "Are you sure you want to delete this account?"
  );

  if (!confirmed) return;

  try {
    await apiRequest(`/api/accounts/${accountId}`, "DELETE");

    setAccounts((prev) =>
      prev.filter((account) => account._id !== accountId)
    );
  } catch (err) {
    alert(err.message);
  }
}

async function handleUpdateBalance(account) {
  const newBalance = prompt(
    "Enter new balance:",
    account.balance
  );

  if (newBalance === null) return;

  const balance = Number(newBalance);

  if (isNaN(balance)) {
    alert("Please enter a valid number.");
    return;
  }

  try {
    const updatedAccount = {
      ...account,
      balance,
    };

    await apiRequest(
      `/api/accounts/${account._id}`,
      "PUT",
      updatedAccount
    );

    setAccounts((prev) =>
      prev.map((a) =>
        a._id === account._id
          ? { ...a, balance }
          : a
      )
    );
  } catch (err) {
    alert(err.message);
  }
}

  return (
    <div style={styles.container}>
      <h2>Dashboard</h2>

      <div>
        {accounts.map((a) => (
        <AccountCard
            key={a._id}
            account={a}
            onUpdateBalance={handleUpdateBalance}
            onDelete={handleDeleteAccount}
        />
        ))}
      </div>

    </div>
  );
}

const styles = {
  container: {
    padding: "20px",
  },
};