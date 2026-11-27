import { useTranslation } from "react-i18next";
import Checkout from "./Checkout";

export default function App() {
  const { t } = useTranslation();
  return (
    <main>
      <button>{t("auth.login")}</button>
      <p className="hint">{t("auth.passwordHint")}</p>
      <Checkout />
    </main>
  );
}
