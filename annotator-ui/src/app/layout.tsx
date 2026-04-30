import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Study 3 Annotator",
  description: "Human evaluation for judge calibration",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
