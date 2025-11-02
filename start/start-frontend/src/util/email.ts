import api from "@/util/request"
import type { Mail,ActiveMail } from "@/types/email.ts"
export function syncEmail() {
  return api.get("/email/sync")
}
export function getEmailList() {
  return api.get<Mail[]>("/email/show")
}
export function getEmailById(uid: number) {
    return api.get<ActiveMail[]>(`/email/show/${uid}`)
}