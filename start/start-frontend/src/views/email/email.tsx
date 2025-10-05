// Email.tsx
import {useState} from "react"
import {Card, Layout, List, Typography} from "antd"
import {MailOutlined} from "@ant-design/icons"
import type {Mail} from "@/types/email.ts"
import styles from "./Email.module.scss"
import {useEmail} from "@/context/EmailContext.tsx" // ← 引入 sass

const {Sider, Content} = Layout
const {Title, Text} = Typography


export function Email() {
    const [activeId, setActiveId] = useState<number | null>(null)
    const {email_list} = useEmail()
    const activeMail = email_list.find((m) => m.id === activeId) ?? null


    return (
        <Layout className={styles.layout}>
            {/* 左侧列表 */}
            <Sider className={styles.sider} theme="light">
                <List<Mail>
                    dataSource={email_list}
                    split
                    renderItem={(mail) => (
                        <List.Item
                            className={`${styles.listItem} ${mail.id === activeId ? styles.active : ""}`}
                            onClick={() => setActiveId(mail.id)}
                        >
                            {/* 左侧：图标 + 内容 */}
                            <div className={styles.leftWrap}>
                                <MailOutlined className={styles.avatar}/>
                                <div className={styles.textWrap}>
                                    <div className={styles.subject}>{mail.subject}</div>
                                </div>
                            </div>

                            {/* 右侧：日期 */}
                            <div className={styles.date}>{mail.date}</div>
                        </List.Item>
                    )}
                />
            </Sider>

            {/* 右侧详情 */}
            <Content className={styles.content}>
                {activeMail ? (
                    <Card className={styles.card}>
                        <Title level={3} style={{marginBottom: 8}}>
                            {activeMail.subject}
                        </Title>
                        <Text type="secondary">发件人：{activeMail.from}</Text>
                        <div
                            style={{marginTop: 24, whiteSpace: "pre-wrap", lineHeight: 1.8}}
                        >
                            {activeMail.body}
                        </div>
                    </Card>
                ) : (
                    <Card className={`${styles.card} ${styles.placeholder}`}>
                        <Text type="secondary" style={{fontSize: 16}}>
                            请选择一封邮件
                        </Text>
                    </Card>
                )}
            </Content>
        </Layout>
    )
}
