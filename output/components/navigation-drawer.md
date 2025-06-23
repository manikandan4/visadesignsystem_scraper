# navigation-drawer

## Metadata
- **Version**: 0.0.1
- **Description**: Collapsible panel or menu next to page content that links to important pages or features.
- **Category**: components

## Example Sections
1. **Default navigation drawers**
   - Description: 

## Examples
### Default navigation drawer
- **Section**: Default navigation drawers
- **URL**: components/navigation-drawer/default-navigation-drawer
- **Tags**: 
```tsx
import { VisaAccountTiny, VisaChevronDownTiny, VisaChevronUpTiny, VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-navigation-drawer';
const navElAriaLabel = 'Default drawer';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './navigation-drawer',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './navigation-drawer',
  },
];

export const DefaultNavigationDrawer = () => {
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const navDrawerRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <UtilityFragment vMargin={10}>
        <Button onClick={() => navDrawerRef.current?.showModal()}>Open drawer</Button>
      </UtilityFragment>

      <UtilityFragment vMarginHorizontal={0}>
        <Panel
          aria-modal="true"
          ref={navDrawerRef}
          id={id}
          tag="dialog"
          style={
            {
              '--v-panel-inline-size': 'initial',
            } as CSSProperties
          }
        >
          <Nav
            drawer
            orientation="vertical"
            tag="div"
            style={
              {
                inlineSize: '242px',
              } as CSSProperties
            }
          >
            <UtilityFragment vMarginRight={4} vMarginLeft="auto">
              <Button
                aria-label="Close"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => navDrawerRef.current?.close()}
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment
              vFlex
              vFlexCol
              vGap={12}
              vMarginTop={4}
              vMarginRight={16}
              vMarginBottom={16}
              vMarginLeft={24}
            >
              <Link
                aria-label="Visa Application Name Home"
                href="https://www.visa.com"
                id={`${id}-home-link`}
                noUnderline
                style={{ backgroundColor: 'transparent' }}
              >
                <VisaLogo />
                <NavAppName>
                  <Typography variant="subtitle-1">Application Name</Typography>
                </NavAppName>
              </Link>
            </UtilityFragment>
            <nav aria-label={navElAriaLabel}>
              <Tabs orientation="vertical">
                {tabsContent.map(tabContent => (
                  <Tab key={tabContent.id}>
                    <UtilityFragment vMarginLeft={14}>
                      <Button colorScheme="tertiary" element={<a href={tabContent.href}>{tabContent.tabLabel}</a>} />
                    </UtilityFragment>
                  </Tab>
                ))}
              </Tabs>
            </nav>
            <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
              <Divider dividerType="decorative" />
              <Tab tag="div">
                <Button
                  aria-expanded={accountTabOpen}
                  aria-controls={`${id}-account-sub-menu`}
                  aria-label="Alex Miller"
                  buttonSize="large"
                  colorScheme="tertiary"
                  onClick={() => setAccountTabOpen(!accountTabOpen)}
                >
                  <VisaAccountTiny />
                  Alex Miller
                  <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                </Button>
                <UtilityFragment vHide={!accountTabOpen}>
                  <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                    {accountSubItems.map(accountSubItem => (
                      <Tab key={accountSubItem.id} id={accountSubItem.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </Tab>
            </Utility>
          </Nav>
        </Panel>
      </UtilityFragment>
    </>
  );
};

```

### Navigation drawer with active element
- **Section**: Default navigation drawers
- **URL**: components/navigation-drawer/navigation-drawer-with-active-element
- **Tags**: 
```tsx
import { VisaAccountTiny, VisaChevronDownTiny, VisaChevronUpTiny, VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'navigation-drawer-with-active-element';
const navElAriaLabel = 'Drawer with active element';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './navigation-drawer',
    active: true,
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './navigation-drawer',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './navigation-drawer',
  },
];

export const NavigationDrawerWithActiveElement = () => {
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const navDrawerRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <UtilityFragment vMargin={10}>
        <Button onClick={() => navDrawerRef.current?.showModal()}>Open drawer</Button>
      </UtilityFragment>

      <UtilityFragment vMarginHorizontal={0}>
        <Panel
          aria-modal="true"
          ref={navDrawerRef}
          id={id}
          tag="dialog"
          style={
            {
              '--v-panel-inline-size': 'initial',
            } as CSSProperties
          }
        >
          <Nav
            drawer
            orientation="vertical"
            tag="div"
            style={
              {
                inlineSize: '242px',
              } as CSSProperties
            }
          >
            <UtilityFragment vMarginRight={4} vMarginLeft="auto">
              <Button
                aria-label="Close"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => navDrawerRef.current?.close()}
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment
              vFlex
              vFlexCol
              vGap={12}
              vMarginTop={4}
              vMarginRight={16}
              vMarginBottom={16}
              vMarginLeft={24}
            >
              <Link
                aria-label="Visa Application Name Home"
                href="https://www.visa.com"
                id={`${id}-home-link`}
                noUnderline
                style={{ backgroundColor: 'transparent' }}
              >
                <VisaLogo />
                <NavAppName>
                  <Typography variant="subtitle-1">Application Name</Typography>
                </NavAppName>
              </Link>
            </UtilityFragment>
            <nav aria-label={navElAriaLabel}>
              <Tabs orientation="vertical">
                {tabsContent.map(tabContent => (
                  <Tab key={tabContent.id}>
                    <UtilityFragment vMarginLeft={14}>
                      <Button
                        aria-current={tabContent.active ? 'page' : false}
                        colorScheme="tertiary"
                        element={<a href={tabContent.href}>{tabContent.tabLabel}</a>}
                      />
                    </UtilityFragment>
                  </Tab>
                ))}
              </Tabs>
            </nav>
            <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
              <Divider dividerType="decorative" />
              <Tab tag="div">
                <Button
                  aria-expanded={accountTabOpen}
                  aria-controls={`${id}-account-sub-menu`}
                  aria-label="Alex Miller"
                  buttonSize="large"
                  colorScheme="tertiary"
                  onClick={() => setAccountTabOpen(!accountTabOpen)}
                >
                  <VisaAccountTiny />
                  Alex Miller
                  <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                </Button>
                <UtilityFragment vHide={!accountTabOpen}>
                  <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                    {accountSubItems.map(accountSubItem => (
                      <Tab key={accountSubItem.id} id={accountSubItem.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </Tab>
            </Utility>
          </Nav>
        </Panel>
      </UtilityFragment>
    </>
  );
};

```

### Navigation drawer with icons
- **Section**: Default navigation drawers
- **URL**: components/navigation-drawer/navigation-drawer-with-icons
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseTiny,
  VisaStatisticsTiny,
  VisaSettingsTiny,
  VisaSecurityTiny,
  VisaNotesTiny,
  VisaSupportTicketTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'navigation-drawer-with-icons';
const navElAriaLabel = 'Drawer with icons';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './navigation-drawer',
    icon: <VisaStatisticsTiny />,
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './navigation-drawer',
    icon: <VisaSettingsTiny />,
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './navigation-drawer',
    icon: <VisaSecurityTiny />,
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './navigation-drawer',
    icon: <VisaNotesTiny />,
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './navigation-drawer',
    icon: <VisaSupportTicketTiny />,
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './navigation-drawer',
  },
];

export const NavigationDrawerWithIcons = () => {
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const navDrawerRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <UtilityFragment vMargin={10}>
        <Button onClick={() => navDrawerRef.current?.showModal()}>Open drawer</Button>
      </UtilityFragment>

      <UtilityFragment vMarginHorizontal={0}>
        <Panel
          aria-modal="true"
          id={id}
          ref={navDrawerRef}
          tag="dialog"
          style={
            {
              '--v-panel-inline-size': 'initial',
            } as CSSProperties
          }
        >
          <Nav
            drawer
            orientation="vertical"
            tag="div"
            style={
              {
                inlineSize: '242px',
              } as CSSProperties
            }
          >
            <UtilityFragment vMarginRight={4} vMarginLeft="auto">
              <Button
                aria-label="Close"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => navDrawerRef.current?.close()}
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment
              vFlex
              vFlexCol
              vGap={12}
              vMarginTop={4}
              vMarginRight={16}
              vMarginBottom={16}
              vMarginLeft={24}
            >
              <Link
                aria-label="Visa Application Name Home"
                href="https://www.visa.com"
                id={`${id}-home-link`}
                noUnderline
                style={{ backgroundColor: 'transparent' }}
              >
                <VisaLogo />
                <NavAppName>
                  <Typography variant="subtitle-1">Application Name</Typography>
                </NavAppName>
              </Link>
            </UtilityFragment>
            <nav aria-label={navElAriaLabel}>
              <Tabs orientation="vertical">
                {tabsContent.map(tabContent => (
                  <Tab key={tabContent.id}>
                    <UtilityFragment vMarginLeft={14}>
                      <Button
                        colorScheme="tertiary"
                        element={
                          <a href={tabContent.href}>
                            {tabContent.icon}
                            {tabContent.tabLabel}
                          </a>
                        }
                      />
                    </UtilityFragment>
                  </Tab>
                ))}
              </Tabs>
            </nav>
            <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
              <Divider dividerType="decorative" />
              <Tab tag="div">
                <Button
                  aria-expanded={accountTabOpen}
                  aria-controls={`${id}-account-sub-menu`}
                  aria-label="Alex Miller"
                  buttonSize="large"
                  colorScheme="tertiary"
                  onClick={() => setAccountTabOpen(!accountTabOpen)}
                >
                  <VisaAccountTiny />
                  Alex Miller
                  <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                </Button>
                <UtilityFragment vHide={!accountTabOpen}>
                  <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                    {accountSubItems.map(accountSubItem => (
                      <Tab key={accountSubItem.id} id={accountSubItem.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </Tab>
            </Utility>
          </Nav>
        </Panel>
      </UtilityFragment>
    </>
  );
};

```

### Navigation drawer with nested elements
- **Section**: Default navigation drawers
- **URL**: components/navigation-drawer/navigation-drawer-with-nested-elements
- **Tags**: 
```tsx
import { VisaAccountTiny, VisaChevronDownTiny, VisaChevronUpTiny, VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'navigation-drawer-with-nested-elements';
const navElAriaLabel = 'Drawer with nested elements';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './navigation-drawer',
  },
];

export const NavigationDrawerWithNestedElements = () => {
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const [l1Label2Expanded, setL1Label2Expanded] = useState(false);
  const [l1Label4Expanded, setL1Label4Expanded] = useState(false);
  const [l2Label1Expanded, setL2Label1Expanded] = useState(false);
  const navDrawerRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <UtilityFragment vMargin={10}>
        <Button onClick={() => navDrawerRef.current?.showModal()}>Open drawer</Button>
      </UtilityFragment>

      <UtilityFragment vMarginHorizontal={0}>
        <Panel
          aria-modal="true"
          ref={navDrawerRef}
          id={id}
          tag="dialog"
          style={
            {
              '--v-panel-inline-size': 'initial',
            } as CSSProperties
          }
        >
          <Nav
            drawer
            orientation="vertical"
            tag="div"
            style={
              {
                inlineSize: '242px',
              } as CSSProperties
            }
          >
            <UtilityFragment vMarginRight={4} vMarginLeft="auto">
              <Button
                aria-label="Close"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => navDrawerRef.current?.close()}
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment
              vFlex
              vFlexCol
              vGap={12}
              vMarginTop={4}
              vMarginRight={16}
              vMarginBottom={16}
              vMarginLeft={24}
            >
              <Link
                aria-label="Visa Application Name Home"
                href="https://www.visa.com"
                id={`${id}-home-link`}
                noUnderline
                style={{ backgroundColor: 'transparent' }}
              >
                <VisaLogo />
                <NavAppName>
                  <Typography variant="subtitle-1">Application Name</Typography>
                </NavAppName>
              </Link>
            </UtilityFragment>
            <nav aria-label={navElAriaLabel}>
              <Tabs orientation="vertical">
                <Tab>
                  <UtilityFragment vMarginLeft={14}>
                    <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 1</a>} />
                  </UtilityFragment>
                </Tab>
                <Tab>
                  <UtilityFragment vMarginLeft={14}>
                    <Button
                      aria-expanded={l1Label2Expanded}
                      aria-controls={`${id}-l1-label2-sub-menu`}
                      colorScheme="tertiary"
                      onClick={() => setL1Label2Expanded(!l1Label2Expanded)}
                    >
                      L1 label 2
                      <TabSuffix element={l1Label2Expanded ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </Button>
                  </UtilityFragment>
                  <UtilityFragment vHide={!l1Label2Expanded}>
                    <Tabs orientation="vertical" id={`${id}-l1-label2-sub-menu`} aria-hidden={!l1Label2Expanded}>
                      <Tab>
                        <UtilityFragment vMarginLeft={28}>
                          <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L2 label 1</a>} />
                        </UtilityFragment>
                      </Tab>
                      <Tab>
                        <UtilityFragment vMarginLeft={28}>
                          <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L2 label 2</a>} />
                        </UtilityFragment>
                      </Tab>
                    </Tabs>
                  </UtilityFragment>
                </Tab>
                <Tab>
                  <UtilityFragment vMarginLeft={14}>
                    <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 3</a>} />
                  </UtilityFragment>
                </Tab>
                <Tab>
                  <UtilityFragment vMarginLeft={14}>
                    <Button
                      aria-expanded={l1Label4Expanded}
                      aria-controls={`${id}-l1-label4-sub-menu`}
                      colorScheme="tertiary"
                      onClick={() => setL1Label4Expanded(!l1Label4Expanded)}
                    >
                      L1 label 4
                      <TabSuffix element={l1Label4Expanded ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </Button>
                  </UtilityFragment>
                  <UtilityFragment vHide={!l1Label4Expanded}>
                    <Tabs orientation="vertical" id={`${id}-l1-label4-sub-menu`} aria-hidden={!l1Label4Expanded}>
                      <Tab>
                        <UtilityFragment vMarginLeft={28}>
                          <Button
                            aria-expanded={l2Label1Expanded}
                            aria-controls={`${id}-l2-label1-sub-menu`}
                            colorScheme="tertiary"
                            onClick={() => setL2Label1Expanded(!l2Label1Expanded)}
                          >
                            L2 label 1
                            <TabSuffix element={l2Label1Expanded ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                          </Button>
                        </UtilityFragment>
                        <UtilityFragment vHide={!l2Label1Expanded}>
                          <Tabs orientation="vertical" id={`${id}-l2-label1-sub-menu`} aria-hidden={!l2Label1Expanded}>
                            <Tab>
                              <UtilityFragment vMarginLeft={42}>
                                <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L3 label 1</a>} />
                              </UtilityFragment>
                            </Tab>
                            <Tab>
                              <UtilityFragment vMarginLeft={42}>
                                <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L3 label 2</a>} />
                              </UtilityFragment>
                            </Tab>
                            <Tab>
                              <UtilityFragment vMarginLeft={42}>
                                <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L3 label 3</a>} />
                              </UtilityFragment>
                            </Tab>
                          </Tabs>
                        </UtilityFragment>
                      </Tab>
                    </Tabs>
                  </UtilityFragment>
                </Tab>
                <Tab>
                  <UtilityFragment vMarginLeft={14}>
                    <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 5</a>} />
                  </UtilityFragment>
                </Tab>
              </Tabs>
            </nav>
            <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
              <Divider dividerType="decorative" />
              <Tab tag="div">
                <Button
                  aria-expanded={accountTabOpen}
                  aria-controls={`${id}-account-sub-menu`}
                  aria-label="Alex Miller"
                  buttonSize="large"
                  colorScheme="tertiary"
                  onClick={() => setAccountTabOpen(!accountTabOpen)}
                >
                  <VisaAccountTiny />
                  Alex Miller
                  <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                </Button>
                <UtilityFragment vHide={!accountTabOpen}>
                  <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                    {accountSubItems.map(accountSubItem => (
                      <Tab key={accountSubItem.id} id={accountSubItem.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </Tab>
            </Utility>
          </Nav>
        </Panel>
      </UtilityFragment>
    </>
  );
};

```

### Navigation drawer with section titles
- **Section**: Default navigation drawers
- **URL**: components/navigation-drawer/navigation-drawer-with-section-titles
- **Tags**: 
```tsx
import { VisaAccountTiny, VisaChevronDownTiny, VisaChevronUpTiny, VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'navigation-drawer-with-section-titles';
const navElAriaLabel = 'Drawer with section titles';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './navigation-drawer',
  },
];

export const NavigationDrawerWithSectionTitles = () => {
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const navDrawerRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <UtilityFragment vMargin={10}>
        <Button onClick={() => navDrawerRef.current?.showModal()}>Open drawer</Button>
      </UtilityFragment>

      <UtilityFragment vMarginHorizontal={0}>
        <Panel
          aria-modal="true"
          ref={navDrawerRef}
          id={id}
          tag="dialog"
          style={
            {
              '--v-panel-inline-size': 'initial',
            } as CSSProperties
          }
        >
          <Nav
            drawer
            orientation="vertical"
            tag="div"
            style={
              {
                inlineSize: '242px',
              } as CSSProperties
            }
          >
            <UtilityFragment vMarginRight={4} vMarginLeft="auto">
              <Button
                aria-label="Close"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => navDrawerRef.current?.close()}
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment
              vFlex
              vFlexCol
              vGap={12}
              vMarginTop={4}
              vMarginRight={16}
              vMarginBottom={16}
              vMarginLeft={24}
            >
              <Link
                aria-label="Visa Application Name Home"
                href="https://www.visa.com"
                id={`${id}-home-link`}
                noUnderline
                style={{ backgroundColor: 'transparent' }}
              >
                <VisaLogo />
                <NavAppName>
                  <Typography variant="subtitle-1">Application Name</Typography>
                </NavAppName>
              </Link>
            </UtilityFragment>
            <nav aria-label={navElAriaLabel}>
              <Tabs orientation="vertical">
                <Tab>
                  <UtilityFragment>
                    <Tab sectionTitle tag="h2">
                      Section Title 1
                    </Tab>
                  </UtilityFragment>
                  <Tabs orientation="vertical">
                    <Tab>
                      <UtilityFragment >
                        <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 1</a>} />
                      </UtilityFragment>
                    </Tab>
                    <Tab>
                      <UtilityFragment>
                        <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 2</a>} />
                      </UtilityFragment>
                    </Tab>
                    <Tab>
                      <UtilityFragment>
                        <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 3</a>} />
                      </UtilityFragment>
                    </Tab>
                  </Tabs>
                </Tab>
                <Tab>
                  <UtilityFragment>
                    <Tab sectionTitle tag="h2">
                      Section Title 2
                    </Tab>
                  </UtilityFragment>
                  <Tabs orientation="vertical">
                    <Tab>
                      <UtilityFragment>
                        <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 4</a>} />
                      </UtilityFragment>
                    </Tab>
                    <Tab>
                      <UtilityFragment>
                        <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 5</a>} />
                      </UtilityFragment>
                    </Tab>
                    <Tab>
                      <UtilityFragment>
                        <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 6</a>} />
                      </UtilityFragment>
                    </Tab>
                  </Tabs>
                </Tab>
              </Tabs>
            </nav>
            <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
              <Divider dividerType="decorative" />
              <Tab tag="div">
                <Button
                  aria-expanded={accountTabOpen}
                  aria-controls={`${id}-account-sub-menu`}
                  aria-label="Alex Miller"
                  buttonSize="large"
                  colorScheme="tertiary"
                  onClick={() => setAccountTabOpen(!accountTabOpen)}
                >
                  <VisaAccountTiny />
                  Alex Miller
                  <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                </Button>
                <UtilityFragment vHide={!accountTabOpen}>
                  <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                    {accountSubItems.map(accountSubItem => (
                      <Tab key={accountSubItem.id} id={accountSubItem.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </Tab>
            </Utility>
          </Nav>
        </Panel>
      </UtilityFragment>
    </>
  );
};

```

### Navigation drawer with nested elements and section titles
- **Section**: Default navigation drawers
- **URL**: components/navigation-drawer/navigation-drawer-with-nested-elements-and-section-titles
- **Tags**: 
```tsx
import { VisaAccountTiny, VisaChevronDownTiny, VisaChevronUpTiny, VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'navigation-drawer-with-nested-elements-and-section-titles';
const navElAriaLabel = 'Drawer with nested elements and section titles';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './navigation-drawer',
  },
];

export const NavigationDrawerWithNestedElementsAndSectionTitles = () => {
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const [l1Label2Expanded, setL1Label2Expanded] = useState(false);
  const [l2Label2Expanded, setL2Label2Expanded] = useState(false);
  const navDrawerRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <UtilityFragment vMargin={10}>
        <Button onClick={() => navDrawerRef.current?.showModal()}>Open drawer</Button>
      </UtilityFragment>

      <UtilityFragment vMarginHorizontal={0}>
        <Panel
          aria-modal="true"
          ref={navDrawerRef}
          id={id}
          tag="dialog"
          style={
            {
              '--v-panel-inline-size': 'initial',
            } as CSSProperties
          }
        >
          <Nav
            drawer
            orientation="vertical"
            tag="div"
            style={
              {
                inlineSize: '242px',
              } as CSSProperties
            }
          >
            <UtilityFragment vMarginRight={4} vMarginLeft="auto">
              <Button
                aria-label="Close"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => navDrawerRef.current?.close()}
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment
              vFlex
              vFlexCol
              vGap={12}
              vMarginTop={4}
              vMarginRight={16}
              vMarginBottom={16}
              vMarginLeft={24}
            >
              <Link
                aria-label="Visa Application Name Home"
                href="https://www.visa.com"
                id={`${id}-home-link`}
                noUnderline
                style={{ backgroundColor: 'transparent' }}
              >
                <VisaLogo />
                <NavAppName>
                  <Typography variant="subtitle-1">Application Name</Typography>
                </NavAppName>
              </Link>
            </UtilityFragment>
            <nav aria-label={navElAriaLabel}>
              <UtilityFragment vGap={8}>
                <Tabs orientation="vertical">
                  <Tab>
                    <Tab sectionTitle tag="h2">
                      L1 Section Title 1
                    </Tab>
                    <Tabs orientation="vertical">
                      <Tab>
                        <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 1</a>} />
                      </Tab>
                      <Tab>
                        <Button
                          aria-expanded={l1Label2Expanded}
                          aria-controls={`${id}-l1-label2-sub-menu`}
                          colorScheme="tertiary"
                          onClick={() => setL1Label2Expanded(!l1Label2Expanded)}
                        >
                          L1 label 2
                          <TabSuffix element={l1Label2Expanded ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                        </Button>
                        <UtilityFragment vHide={!l1Label2Expanded}>
                          <Tabs orientation="vertical" id={`${id}-l1-label2-sub-menu`} tag="div">
                            <Tab sectionTitle tag="h3">
                              L2 Section Title 1
                            </Tab>
                            <Tabs orientation="vertical">
                              <Tab>
                                <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L2 label 1</a>} />
                              </Tab>
                              <Tab>
                                <Button
                                  aria-expanded={l2Label2Expanded}
                                  aria-controls={`${id}-l2-label2-sub-menu`}
                                  colorScheme="tertiary"
                                  onClick={() => setL2Label2Expanded(!l2Label2Expanded)}
                                >
                                  L2 label 2
                                  <TabSuffix
                                    element={l2Label2Expanded ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
                                  />
                                </Button>

                                <UtilityFragment vHide={!l2Label2Expanded}>
                                  <Tabs orientation="vertical" id={`${id}-l2-label2-sub-menu`} tag="div">
                                    <Tab sectionTitle tag="h4">
                                      L3 Section Title 1
                                    </Tab>
                                    <Tabs orientation="vertical">
                                      <Tab>
                                        <Button
                                          colorScheme="tertiary"
                                          element={<a href="./navigation-drawer">L3 label 1</a>}
                                        />
                                      </Tab>
                                      <Tab>
                                        <Button
                                          colorScheme="tertiary"
                                          element={<a href="./navigation-drawer">L3 label 2</a>}
                                        />
                                      </Tab>
                                    </Tabs>
                                  </Tabs>
                                </UtilityFragment>
                              </Tab>
                            </Tabs>
                          </Tabs>
                        </UtilityFragment>
                      </Tab>
                    </Tabs>
                  </Tab>
                  <Tab>
                    <Tab sectionTitle tag="h2">
                      L1 Section Title 2
                    </Tab>
                    <Tabs orientation="vertical">
                      <Tab>
                        <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 3</a>} />
                      </Tab>
                      <Tab>
                        <Button colorScheme="tertiary" element={<a href="./navigation-drawer">L1 label 4</a>} />
                      </Tab>
                    </Tabs>
                  </Tab>
                </Tabs>
              </UtilityFragment>
            </nav>
            <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
              <Divider dividerType="decorative" />
              <Tab tag="div">
                <Button
                  aria-expanded={accountTabOpen}
                  aria-controls={`${id}-account-sub-menu`}
                  aria-label="Alex Miller"
                  buttonSize="large"
                  colorScheme="tertiary"
                  onClick={() => setAccountTabOpen(!accountTabOpen)}
                >
                  <VisaAccountTiny />
                  Alex Miller
                  <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                </Button>
                <UtilityFragment vHide={!accountTabOpen}>
                  <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                    {accountSubItems.map(accountSubItem => (
                      <Tab key={accountSubItem.id} id={accountSubItem.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </Tab>
            </Utility>
          </Nav>
        </Panel>
      </UtilityFragment>
    </>
  );
};

```

### Alternate navigation drawer
- **Section**: Default navigation drawers
- **URL**: components/navigation-drawer/alternate-navigation-drawer
- **Tags**: 
```tsx
import { VisaAccountTiny, VisaChevronDownTiny, VisaChevronUpTiny, VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'alternate-navigation-drawer';
const navElAriaLabel = 'Alternate drawer';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './navigation-drawer',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './navigation-drawer',
  },
];

export const AlternateNavigationDrawer = () => {
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const navDrawerRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <UtilityFragment vMargin={10}>
        <Button onClick={() => navDrawerRef.current?.showModal()}>Open drawer</Button>
      </UtilityFragment>

      <UtilityFragment vMarginHorizontal={0}>
        <Panel
          aria-modal="true"
          ref={navDrawerRef}
          id={id}
          tag="dialog"
          style={
            {
              '--v-panel-inline-size': 'initial',
            } as CSSProperties
          }
        >
          <Nav
            alternate
            drawer
            orientation="vertical"
            tag="div"
            style={
              {
                inlineSize: '242px',
              } as CSSProperties
            }
          >
            <UtilityFragment vMarginRight={4} vMarginLeft="auto">
              <Button
                aria-label="Close"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => navDrawerRef.current?.close()}
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment
              vFlex
              vFlexCol
              vGap={12}
              vMarginTop={4}
              vMarginRight={16}
              vMarginBottom={16}
              vMarginLeft={24}
            >
              <Link
                aria-label="Visa Application Name Home"
                href="https://www.visa.com"
                id={`${id}-home-link`}
                noUnderline
                style={{ backgroundColor: 'transparent' }}
              >
                <VisaLogo />
                <NavAppName>
                  <Typography variant="subtitle-1">Application Name</Typography>
                </NavAppName>
              </Link>
            </UtilityFragment>
            <nav aria-label={navElAriaLabel}>
              <Tabs orientation="vertical">
                {tabsContent.map(tabContent => (
                  <Tab key={tabContent.id}>
                    <UtilityFragment vMarginLeft={14}>
                      <Button colorScheme="tertiary" element={<a href={tabContent.href}>{tabContent.tabLabel}</a>} />
                    </UtilityFragment>
                  </Tab>
                ))}
              </Tabs>
            </nav>
            <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
              <Divider dividerType="decorative" />
              <Tab tag="div">
                <Button
                  aria-expanded={accountTabOpen}
                  aria-controls={`${id}-account-sub-menu`}
                  aria-label="Alex Miller"
                  buttonSize="large"
                  colorScheme="tertiary"
                  onClick={() => setAccountTabOpen(!accountTabOpen)}
                >
                  <VisaAccountTiny />
                  Alex Miller
                  <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                </Button>
                <UtilityFragment vHide={!accountTabOpen}>
                  <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                    {accountSubItems.map(accountSubItem => (
                      <Tab key={accountSubItem.id} id={accountSubItem.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </Tab>
            </Utility>
          </Nav>
        </Panel>
      </UtilityFragment>
    </>
  );
};

```

### Alternate navigation drawer with active element
- **Section**: Default navigation drawers
- **URL**: components/navigation-drawer/alternate-navigation-drawer-with-active-element
- **Tags**: 
```tsx
import { VisaAccountTiny, VisaChevronDownTiny, VisaChevronUpTiny, VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'alternate-navigation-drawer-with-active-element';
const navElAriaLabel = 'Alternate drawer with active element';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './navigation-drawer',
    active: true,
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './navigation-drawer',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './navigation-drawer',
  },
];

export const AlternateNavigationDrawerWithActiveElement = () => {
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const navDrawerRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <UtilityFragment vMargin={10}>
        <Button onClick={() => navDrawerRef.current?.showModal()}>Open drawer</Button>
      </UtilityFragment>

      <UtilityFragment vMarginHorizontal={0}>
        <Panel
          aria-modal="true"
          ref={navDrawerRef}
          id={id}
          tag="dialog"
          style={
            {
              '--v-panel-inline-size': 'initial',
            } as CSSProperties
          }
        >
          <Nav
            alternate
            drawer
            orientation="vertical"
            tag="div"
            style={
              {
                inlineSize: '242px',
              } as CSSProperties
            }
          >
            <UtilityFragment vMarginRight={4} vMarginLeft="auto">
              <Button
                aria-label="Close"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => navDrawerRef.current?.close()}
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment
              vFlex
              vFlexCol
              vGap={12}
              vMarginTop={4}
              vMarginRight={16}
              vMarginBottom={16}
              vMarginLeft={24}
            >
              <Link
                aria-label="Visa Application Name Home"
                href="https://www.visa.com"
                id={`${id}-home-link`}
                noUnderline
                style={{ backgroundColor: 'transparent' }}
              >
                <VisaLogo />
                <NavAppName>
                  <Typography variant="subtitle-1">Application Name</Typography>
                </NavAppName>
              </Link>
            </UtilityFragment>
            <nav aria-label={navElAriaLabel}>
              <Tabs orientation="vertical">
                {tabsContent.map(tabContent => (
                  <Tab key={tabContent.id}>
                    <UtilityFragment vMarginLeft={14}>
                      <Button
                        aria-current={tabContent.active ? 'page' : false}
                        colorScheme="tertiary"
                        element={<a href={tabContent.href}>{tabContent.tabLabel}</a>}
                      />
                    </UtilityFragment>
                  </Tab>
                ))}
              </Tabs>
            </nav>
            <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
              <Divider dividerType="decorative" />
              <Tab tag="div">
                <Button
                  aria-expanded={accountTabOpen}
                  aria-controls={`${id}-account-sub-menu`}
                  aria-label="Alex Miller"
                  buttonSize="large"
                  colorScheme="tertiary"
                  onClick={() => setAccountTabOpen(!accountTabOpen)}
                >
                  <VisaAccountTiny />
                  Alex Miller
                  <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                </Button>
                <UtilityFragment vHide={!accountTabOpen}>
                  <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                    {accountSubItems.map(accountSubItem => (
                      <Tab key={accountSubItem.id} id={accountSubItem.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </Tab>
            </Utility>
          </Nav>
        </Panel>
      </UtilityFragment>
    </>
  );
};

```

### Alternate navigation drawer with icons
- **Section**: Default navigation drawers
- **URL**: components/navigation-drawer/alternate-navigation-drawer-with-icons
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseTiny,
  VisaStatisticsTiny,
  VisaSettingsTiny,
  VisaSecurityTiny,
  VisaNotesTiny,
  VisaSupportTicketTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'alternate-navigation-drawer-with-icons';
const navElAriaLabel = 'Alternate drawer with icons';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './navigation-drawer',
    icon: <VisaStatisticsTiny />,
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './navigation-drawer',
    icon: <VisaSettingsTiny />,
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './navigation-drawer',
    icon: <VisaSecurityTiny />,
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './navigation-drawer',
    icon: <VisaNotesTiny />,
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './navigation-drawer',
    icon: <VisaSupportTicketTiny />,
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './navigation-drawer',
  },
];

export const AlternateNavigationDrawerWithIcons = () => {
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const navDrawerRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <UtilityFragment vMargin={10}>
        <Button onClick={() => navDrawerRef.current?.showModal()}>Open drawer</Button>
      </UtilityFragment>

      <UtilityFragment vMarginHorizontal={0}>
        <Panel
          aria-modal="true"
          ref={navDrawerRef}
          id={id}
          tag="dialog"
          style={
            {
              '--v-panel-inline-size': 'initial',
            } as CSSProperties
          }
        >
          <Nav
            alternate
            drawer
            orientation="vertical"
            tag="div"
            style={
              {
                inlineSize: '242px',
              } as CSSProperties
            }
          >
            <UtilityFragment vMarginRight={4} vMarginLeft="auto">
              <Button
                aria-label="Close"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => navDrawerRef.current?.close()}
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment
              vFlex
              vFlexCol
              vGap={12}
              vMarginTop={4}
              vMarginRight={16}
              vMarginBottom={16}
              vMarginLeft={24}
            >
              <Link
                aria-label="Visa Application Name Home"
                href="https://www.visa.com"
                id={`${id}-home-link`}
                noUnderline
                style={{ backgroundColor: 'transparent' }}
              >
                <VisaLogo />
                <NavAppName>
                  <Typography variant="subtitle-1">Application Name</Typography>
                </NavAppName>
              </Link>
            </UtilityFragment>
            <nav aria-label={navElAriaLabel}>
              <Tabs orientation="vertical">
                {tabsContent.map(tabContent => (
                  <Tab key={tabContent.id}>
                    <UtilityFragment vMarginLeft={14}>
                      <Button
                        colorScheme="tertiary"
                        element={
                          <a href={tabContent.href}>
                            {tabContent.icon}
                            {tabContent.tabLabel}
                          </a>
                        }
                      />
                    </UtilityFragment>
                  </Tab>
                ))}
              </Tabs>
            </nav>
            <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
              <Divider dividerType="decorative" />
              <Tab tag="div">
                <Button
                  aria-expanded={accountTabOpen}
                  aria-controls={`${id}-account-sub-menu`}
                  aria-label="Alex Miller"
                  buttonSize="large"
                  colorScheme="tertiary"
                  onClick={() => setAccountTabOpen(!accountTabOpen)}
                >
                  <VisaAccountTiny />
                  Alex Miller
                  <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                </Button>
                <UtilityFragment vHide={!accountTabOpen}>
                  <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                    {accountSubItems.map(accountSubItem => (
                      <Tab key={accountSubItem.id} id={accountSubItem.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </Tab>
            </Utility>
          </Nav>
        </Panel>
      </UtilityFragment>
    </>
  );
};

```

## Property Sections
### Nav
- **Selector**: <Nav />
- **Description**: Menu or panel at the top or next to page content that links to important pages or features.

### tabs
- **Selector**: <Tabs />
- **Description**: 

## Properties
### alternate
- **Section**: Nav
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate

### drawer
- **Section**: Nav
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Drawer

### ref
- **Section**: Nav
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Nav
- **Type**: ElementType
- **Default**: nav
- **Required**: false
- **Description**: Tag of Component

