import { createContext, useContext } from "react"
import type { Mail } from "@/types/email"

export interface EmailCtxValue {
  email_list: Mail[]
  get_email_list: () => Promise<void>
}

export const EmailContext = createContext<EmailCtxValue>({
  email_list: [],
  get_email_list: async () => {},
})

export const useEmail = () => useContext(EmailContext)
