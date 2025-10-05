import Email from "@/views/email"
import { EmailContextProvider } from "@/context/EmailContextProvider.tsx"
function App() {
  return (
    <EmailContextProvider>
      <Email />
    </EmailContextProvider>
  )
}

export default App
