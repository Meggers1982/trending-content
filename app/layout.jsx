import "./globals.css";

export const metadata = {
  title: "Trending Content OS",
  description: "Health and wellness trend radar for editorial planning"
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
