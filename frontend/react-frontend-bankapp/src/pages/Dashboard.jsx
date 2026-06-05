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

async function handleDeposit(account) {
  const newBalance = prompt(
    "Enter deposit amount:"
  );

  if (newBalance === null) return;

  const balance_change = Number(newBalance);

  if (isNaN(balance_change)) {
    alert("Please enter a valid number.");
    return;
  }

  try {
    const updatedAccount = {
      balance_change: balance_change
    };

    await apiRequest(
      `/api/accounts/${account._id}/deposit`,
      "PUT",
      updatedAccount
    );

    setAccounts((prev) =>
      prev.map((a) =>
        a._id === account._id
          ? { ...a, balance: balance_change + a.balance }
          : a
      )
    );
  } catch (err) {
    alert(err.message);
  }
}

async function handleWithdraw(account) {
  const newBalance = prompt(
    "Enter withdraw amount:"
  );

  if (newBalance === null) return;

  const balance_change = Number(newBalance);

  if (isNaN(balance_change)) {
    alert("Please enter a valid number.");
    return;
  }

  try {
    const updatedAccount = {
      balance_change: balance_change
    };

    await apiRequest(
      `/api/accounts/${account._id}/withdraw`,
      "PUT",
      updatedAccount
    );

    setAccounts((prev) =>
      prev.map((a) =>
        a._id === account._id
          ? { ...a, balance: a.balance - balance_change }
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
            onDeposit={handleDeposit}
            onWithdraw={handleWithdraw}
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