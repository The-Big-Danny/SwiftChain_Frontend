import './global.css';
import { QueryProvider } from '@/components/providers/QueryProvider';
import { ThemeToggle } from '@/components/ui/ThemeToggle';
import { Providers } from './providers';

export const metadata = {
  title: 'SwiftChain',
  description: 'Blockchain-Powered Logistics Platform',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <Providers>
          <QueryProvider>
            <div className="fixed right-4 top-4 z-50">
              <ThemeToggle />
            </div>
            {children}
          </QueryProvider>
        </Providers>
      </body>
    </html>
  );
}