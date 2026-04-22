import { DisconnectButton } from '@/components/wallet/DisconnectButton';

export default function AdminDashboardPage() {
  return (
    <div>
      <h1>Admin Dashboard</h1>
      {/* Wallet session controls — see hooks/useWallet.ts for disconnect logic */}
      <DisconnectButton />
    </div>
  );
}