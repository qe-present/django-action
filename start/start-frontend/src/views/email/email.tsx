import { useState} from "react"
import {Card, Layout, List, Typography} from "antd"
import {MailOutlined} from "@ant-design/icons"
import type {ActiveMail,Mail} from "@/types/email.ts"
import styles from "./Email.module.scss"
import {useEmail} from "@/context/EmailContext.tsx" // ← 引入 sass

const {Sider, Content} = Layout
const {Title, Text} = Typography


export function Email() {
    const [activeMail, setActiveMail] = useState<ActiveMail | null>(null);
    const [activeId, setActiveId] = useState<number | null>(null)
    const {email_list,get_email_by_id} = useEmail()
    const handleSelect=async (id: number) => {
        setActiveId(id)
        const res:ActiveMail[]=await get_email_by_id(id);
        console.log(res[0]);
        setActiveMail(res[0]);

    }


    return (
        <Layout className={styles.layout}>
            <Sider className={styles.sider} theme="light">
                <List<Mail>
                    dataSource={email_list}
                    split
                    renderItem={(mail) => (
                        <List.Item
                            className={`${styles.listItem} ${mail.id === activeId ? styles.active : ""}`}
                            onClick={() => handleSelect(mail.id)}
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
            <Content className={styles.content}>
                {activeMail ? (
                    <Card className={styles.card}>
                        <Title level={3} style={{marginBottom: 8}}>
                            {activeMail.subject}
                        </Title>
                        <Text type="secondary">发件人：{activeMail.from_email}</Text>
                        <div
                          style={{ marginTop: 24, lineHeight: 1.8 }}
                          dangerouslySetInnerHTML={{ __html:activeMail.html.trim() ? activeMail.html : activeMail.text }}
                        />
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
