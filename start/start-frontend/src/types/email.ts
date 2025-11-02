export type Mail = {
  id: number
  date: string
  subject: string
}
export type ActiveMail={
    id: number
    from_name: string
    from_email: string
    date: string
    subject: string
    html: string
    text: string
}