import { createContext, useContext } from "react"
import type { Mail } from "@/types/email"

export interface EmailCtxValue {
  email_list: Mail[]
  get_email_list: () => Promise<void>,
  get_email_by_id: (id:number) => Promise<any>
}

export const EmailContext = createContext<EmailCtxValue>({
  email_list: [],
  get_email_list: async () => {},
  get_email_by_id: async (id:number) => {}
})

export const useEmail = () => useContext(EmailContext)
