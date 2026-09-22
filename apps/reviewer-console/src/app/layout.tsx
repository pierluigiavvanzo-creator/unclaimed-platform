import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Unclaimed Insurance · M3 Operations Console",
  description: "Read-only governance and provenance visibility for the M3 platform slice.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
