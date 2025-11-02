import Email from "@/views/email"
import {EmailContextProvider} from "@/context/EmailContextProvider.tsx";

export default function Home() {
  return (
    <EmailContextProvider>
      <Email />
    </EmailContextProvider>
  )
}
