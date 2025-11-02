import { useState, useEffect } from "react"
import type { FC } from "react"
import { getEmailList,getEmailById } from "@/util/email"
import { EmailContext } from "./EmailContext"
import type { Mail } from "@/types/email"

export const EmailContextProvider: FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [email_list, setEmailList] = useState<Mail[]>([])

  const get_email_list = async () => {
    try {
      const res = await getEmailList()
      setEmailList(res.data ?? [])
    } catch {
      setEmailList([])
    }
  }
  const get_email_by_id=async (id:number)=>{
    try {
        const res = await getEmailById(id)
        return res.data
    }
    catch{

    }
  }

  useEffect(() => {
    get_email_list()
  }, [])

  return (
    <EmailContext.Provider value={{ email_list, get_email_list,get_email_by_id }}>
      {children}
    </EmailContext.Provider>
  )
}
