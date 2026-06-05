export default function AccountCard({
  account,
  onDelete,
  onUpdateBalance,
  onDeposit,
  onWithdraw
}) {
  return (
    <div style={styles.card}>
      <h3>{account.account_type} Account</h3>

      <h2>${account.balance.toFixed(2)}</h2>

      <div style={styles.buttonContainer}>
        <button
          onClick={() => onDeposit(account)}
        >
          Deposit
        </button>

        <button
          onClick={() => onWithdraw(account)}
        >
          Withdraw
        </button>

        <button
          onClick={() => onDelete(account._id)}
        >
          Delete Account
        </button>
      </div>
    </div>
  );
}

const styles = {
  card: {
    padding: "16px",
    borderRadius: "10px",
    background: "#f1f5f9",
    marginBottom: "10px",
  },
  buttonContainer: {
    display: "flex",
    gap: "10px",
    marginTop: "10px",
  },
};