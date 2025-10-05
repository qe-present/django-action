import { useState, useEffect } from "react"
import type { FC } from "react"
import { getEmailList } from "@/util/email"
import { EmailContext } from "./EmailContext"
import type { Mail } from "@/types/email"

export const EmailContextProvider: FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [email_list, setEmailList] = useState<Mail[]>([])

  const get_email_list = async () => {
    try {
      const res = await getEmailList()
      console.log("Fetched email list:", res.data)
      setEmailList(res.data ?? [])
    } catch {
      setEmailList([])
    }
  }

  useEffect(() => {
    get_email_list()
  }, [])

  return (
    <EmailContext.Provider value={{ email_list, get_email_list }}>
      {children}
    </EmailContext.Provider>
  )
}
