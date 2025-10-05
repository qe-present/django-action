import { useState } from "react"
import { Outlet } from "react-router"
import { Layout, Menu } from "antd"
import {
  AppstoreOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
} from "@ant-design/icons"

const { Header, Sider, Content } = Layout

export default function MainLayout() {
  const [collapsed, setCollapsed] = useState(false)

  const autoCollapse = () => setCollapsed(true) // 离开左侧
  const autoExpand = () => setCollapsed(false) // 进入左侧

  return (
    <Layout style={{ minHeight: "100vh" }}>
      {/* 左侧菜单 */}
      <Sider
        trigger={null}
        collapsible
        collapsed={collapsed}
        onMouseEnter={autoExpand} /* 🚀 鼠标进来展开 */
        onMouseLeave={autoCollapse} /* 🚀 鼠标离开收缩 */
      >
        <div
          style={{
            height: 32,
            margin: "16px 8px",
            background: "rgba(255,255,255,.3)",
            borderRadius: 4,
          }}
        />
        <Menu
          theme="dark"
          mode="inline"
          defaultSelectedKeys={["1"]}
          items={[
            {
              key: "1",
              icon: <AppstoreOutlined />,
              label: "首页",
              onClick: () => (window.location.href = "/"),
            },
          ]}
        />
      </Sider>

      <Layout>
        {/* 顶部 */}
        <Header style={{ background: "#fff", padding: 0 }}>
          {collapsed ? (
            <MenuUnfoldOutlined
              style={{ fontSize: 18, marginLeft: 24 }}
              onClick={() => setCollapsed(false)}
            />
          ) : (
            <MenuFoldOutlined
              style={{ fontSize: 18, marginLeft: 24 }}
              onClick={() => setCollapsed(true)}
            />
          )}
        </Header>

        {/* 内容区 */}
        <Content style={{ margin: 24, padding: 24, background: "#fff" }}>
          <Outlet />
        </Content>
      </Layout>
    </Layout>
  )
}
