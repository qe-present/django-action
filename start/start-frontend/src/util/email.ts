import api from "@/util/request"
import type { Mail } from "@/types/email.ts"
export function syncEmail() {
  return api.get("/email/sync")
}
export function getEmailList() {
  return api.get<Mail[]>("/email/show")
}
