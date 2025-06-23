# vertical-navigation

## Metadata
- **Version**: 0.0.1
- **Description**: Menu or panel next to the page content that links to important pages or features.
- **Category**: components

## Example Sections
1. **Default vertical navigations**
   - Description: 
2. **Custom vertical navigation**
   - Description: 

## Examples
### Default vertical navigation
- **Section**: Default vertical navigations
- **URL**: components/vertical-navigation/default-vertical-navigation
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaMediaFastForwardTiny,
  VisaMediaRewindTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
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
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-vertical-navigation';
const navRegionAriaLabel = 'Default vertical navigation';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './vertical-navigation',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const DefaultVerticalNavigation = () => {
  const [navExpanded, setNavExpanded] = useState(true);
  const [accountTabOpen, setAccountTabOpen] = useState(false);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} orientation="vertical" tag="header">
          {navExpanded && (
            <Link skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <UtilityFragment
                vFlex
                vFlexCol
                vGap={12}
                vMarginTop={16}
                vMarginRight={16}
                vMarginBottom={30}
                vMarginLeft={20}
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
              <nav aria-label={navRegionAriaLabel}>
                <UtilityFragment vGap={8}>
                  <Tabs orientation="vertical">
                    {tabsContent.map(tabContent => (
                      <Tab key={tabContent.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href="./vertical-navigation">{tabContent.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </nav>
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            {navExpanded && (
              <>
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
              </>
            )}
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
  );
};

```

### Vertical navigation with active element
- **Section**: Default vertical navigations
- **URL**: components/vertical-navigation/vertical-navigation-with-active-element
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaMediaFastForwardTiny,
  VisaMediaRewindTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
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
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'vertical-navigation-with-active-element';
const navRegionAriaLabel = 'Vertical navigation with active element';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    active: true,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './vertical-navigation',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const VerticalNavigationWithActiveElement = () => {
  const [navExpanded, setNavExpanded] = useState(true);
  const [accountTabOpen, setAccountTabOpen] = useState(false);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} orientation="vertical" tag="header">
          {navExpanded && (
            <Link skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <UtilityFragment
                vFlex
                vFlexCol
                vGap={12}
                vMarginTop={16}
                vMarginRight={16}
                vMarginBottom={30}
                vMarginLeft={20}
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
              <nav aria-label={navRegionAriaLabel}>
                <UtilityFragment vGap={8}>
                  <Tabs orientation="vertical">
                    {tabsContent.map(tabContent => (
                      <Tab key={tabContent.id}>
                        <Button
                          colorScheme="tertiary"
                          aria-current={tabContent.active ? 'page' : false}
                          element={<a href={tabContent.href}>{tabContent.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </nav>
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            {navExpanded && (
              <>
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
              </>
            )}
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
  );
};

```

### Vertical navigation with icons
- **Section**: Default vertical navigations
- **URL**: components/vertical-navigation/vertical-navigation-with-icons
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaMediaFastForwardTiny,
  VisaMediaRewindTiny,
  VisaStatisticsTiny,
  VisaSettingsTiny,
  VisaSecurityTiny,
  VisaNotesTiny,
  VisaSupportTicketTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
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
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'vertical-navigation-with-icons';
const navRegionAriaLabel = 'Vertical navigation with icons';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0}`,
    icon: <VisaStatisticsTiny />,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1}`,
    icon: <VisaSettingsTiny />,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2}`,
    icon: <VisaSecurityTiny />,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3}`,
    icon: <VisaNotesTiny />,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4}`,
    icon: <VisaSupportTicketTiny />,
    href: './vertical-navigation',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const VerticalNavigationWithIcons = () => {
  const [navExpanded, setNavExpanded] = useState(true);
  const [accountTabOpen, setAccountTabOpen] = useState(false);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} orientation="vertical" tag="header">
          {navExpanded && (
            <Link skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <UtilityFragment
                vFlex
                vFlexCol
                vGap={12}
                vMarginTop={16}
                vMarginRight={16}
                vMarginBottom={30}
                vMarginLeft={20}
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
              <nav aria-label={navRegionAriaLabel}>
                <UtilityFragment vGap={8}>
                  <Tabs orientation="vertical">
                    {tabsContent.map(tabContent => (
                      <Tab key={tabContent.id}>
                        <Button
                          colorScheme="tertiary"
                          element={
                            <a href={tabContent.href}>
                              {tabContent.icon}
                              {tabContent.tabLabel}
                            </a>
                          }
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </nav>
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            {navExpanded && (
              <>
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
              </>
            )}
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
  );
};

```

### Vertical navigation with nested elements
- **Section**: Default vertical navigations
- **URL**: components/vertical-navigation/vertical-navigation-with-nested-elements
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaMediaFastForwardTiny,
  VisaMediaRewindTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
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
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'vertical-navigation-with-nested-elements';
const navRegionAriaLabel = 'Vertical navigation with nested elements';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const VerticalNavigationWithNestedElements = () => {
  const [navExpanded, setNavExpanded] = useState(true);
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const [l1Label2Expanded, setL1Label2Expanded] = useState(false);
  const [l1Label4Expanded, setL1Label4Expanded] = useState(false);
  const [l2Label1Expanded, setL2Label1Expanded] = useState(false);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} orientation="vertical" tag="header">
          {navExpanded && (
            <Link skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <UtilityFragment
                vFlex
                vFlexCol
                vGap={12}
                vMarginTop={16}
                vMarginRight={16}
                vMarginBottom={30}
                vMarginLeft={20}
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
              <nav aria-label={navRegionAriaLabel}>
                <UtilityFragment vGap={8}>
                  <Tabs orientation="vertical">
                    <Tab>
                      <Button colorScheme="tertiary" element={<a href="./vertical-navigation">L1 label 1</a>} />
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
                        <Tabs orientation="vertical" id={`${id}-l1-label2-sub-menu`} aria-hidden={!l1Label2Expanded}>
                          <Tab>
                            <Button colorScheme="tertiary" element={<a href="./vertical-navigation">L2 label 1</a>} />
                          </Tab>
                          <Tab>
                            <Button colorScheme="tertiary" element={<a href="./vertical-navigation">L2 label 2</a>} />
                          </Tab>
                        </Tabs>
                      </UtilityFragment>
                    </Tab>
                    <Tab>
                      <Button colorScheme="tertiary" element={<a href="./vertical-navigation">L1 label 3</a>} />
                    </Tab>
                    <Tab>
                      <Button
                        aria-expanded={l1Label4Expanded}
                        aria-controls={`${id}-l1-label4-sub-menu`}
                        colorScheme="tertiary"
                        onClick={() => setL1Label4Expanded(!l1Label4Expanded)}
                      >
                        L1 label 4
                        <TabSuffix element={l1Label4Expanded ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                      </Button>
                      <UtilityFragment vHide={!l1Label4Expanded}>
                        <Tabs orientation="vertical" id={`${id}-l1-label4-sub-menu`} aria-hidden={!l1Label4Expanded}>
                          <Tab>
                            <Button
                              aria-expanded={l2Label1Expanded}
                              aria-controls={`${id}-l2-label1-sub-menu`}
                              colorScheme="tertiary"
                              onClick={() => setL2Label1Expanded(!l2Label1Expanded)}
                            >
                              L2 label 1
                              <TabSuffix element={l2Label1Expanded ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                            </Button>

                            <UtilityFragment vHide={!l2Label1Expanded}>
                              <Tabs
                                orientation="vertical"
                                id={`${id}-l2-label1-sub-menu`}
                                aria-hidden={!l2Label1Expanded}
                              >
                                <Tab>
                                  <Button
                                    colorScheme="tertiary"
                                    element={<a href="./vertical-navigation">L3 label 1</a>}
                                  />
                                </Tab>
                                <Tab>
                                  <Button
                                    colorScheme="tertiary"
                                    element={<a href="./vertical-navigation">L3 label 2</a>}
                                  />
                                </Tab>
                                <Tab>
                                  <Button
                                    colorScheme="tertiary"
                                    element={<a href="./vertical-navigation">L3 label 3</a>}
                                  />
                                </Tab>
                              </Tabs>
                            </UtilityFragment>
                          </Tab>
                        </Tabs>
                      </UtilityFragment>
                    </Tab>
                    <Tab>
                      <Button colorScheme="tertiary" element={<a href="./vertical-navigation">L1 label 5</a>} />
                    </Tab>
                  </Tabs>
                </UtilityFragment>
              </nav>
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            {navExpanded && (
              <>
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
              </>
            )}
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
  );
};

```

### Vertical navigation with section titles
- **Section**: Default vertical navigations
- **URL**: components/vertical-navigation/vertical-navigation-with-section-titles
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaMediaFastForwardTiny,
  VisaMediaRewindTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
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
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'vertical-navigation-with-section-titles';
const navRegionAriaLabel = 'Vertical navigation with section titles';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const VerticalNavigationWithSectionTitles = () => {
  const [navExpanded, setNavExpanded] = useState(true);
  const [accountTabOpen, setAccountTabOpen] = useState(false);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} orientation="vertical" tag="header">
          {navExpanded && (
            <Link skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <UtilityFragment
                vFlex
                vFlexCol
                vGap={12}
                vMarginTop={16}
                vMarginRight={16}
                vMarginBottom={30}
                vMarginLeft={20}
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
              <nav aria-label={navRegionAriaLabel}>
                <UtilityFragment vGap={8}>
                  <Tabs orientation="vertical">
                    <Tab>
                      <UtilityFragment>
                        <Tab sectionTitle tag="h2">
                          Section Title 1
                        </Tab>
                      </UtilityFragment>
                      <Tabs orientation="vertical">
                        <Tab>
                          <UtilityFragment>
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
                </UtilityFragment>
              </nav>
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            {navExpanded && (
              <>
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
              </>
            )}
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
  );
};

```

### Vertical navigation with nested elements and section titles
- **Section**: Default vertical navigations
- **URL**: components/vertical-navigation/vertical-navigation-with-nested-elements-and-section-titles
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaMediaFastForwardTiny,
  VisaMediaRewindTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
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
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'vertical-navigation-with-nested-elements-and-section-titles';
const navRegionAriaLabel = 'Vertical navigation with nested elements and section titles';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const VerticalNavigationWithNestedElementsAndSectionTitles = () => {
  const [navExpanded, setNavExpanded] = useState(true);
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const [l1Label2Expanded, setL1Label2Expanded] = useState(false);
  const [l2Label2Expanded, setL2Label2Expanded] = useState(false);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} orientation="vertical" tag="header">
          {navExpanded && (
            <Link skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <UtilityFragment
                vFlex
                vFlexCol
                vGap={12}
                vMarginTop={16}
                vMarginRight={16}
                vMarginBottom={30}
                vMarginLeft={20}
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
              <nav aria-label={navRegionAriaLabel}>
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
                            <Tabs
                              orientation="vertical"
                              id={`${id}-l1-label2-sub-menu`}
                              tag="div"
                            >
                              <Tab sectionTitle tag="h3">
                                L2 Section Title 1
                              </Tab>
                              <Tabs orientation="vertical">
                                <Tab>
                                  <Button
                                    colorScheme="tertiary"
                                    element={<a href="./navigation-drawer">L2 label 1</a>}
                                  />
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
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            {navExpanded && (
              <>
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
              </>
            )}
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
  );
};

```

### Alternate vertical navigation
- **Section**: Default vertical navigations
- **URL**: components/vertical-navigation/alternate-vertical-navigation
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaMediaFastForwardTiny,
  VisaMediaRewindTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
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
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'alternate-vertical-navigation';
const navRegionAriaLabel = 'Alternate vertical navigation';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './vertical-navigation',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const AlternateVerticalNavigation = () => {
  const [navExpanded, setNavExpanded] = useState(true);
  const [accountTabOpen, setAccountTabOpen] = useState(false);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} alternate orientation="vertical" tag="header">
          {navExpanded && (
            <Link alternate skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <UtilityFragment
                vFlex
                vFlexCol
                vGap={12}
                vMarginTop={16}
                vMarginRight={16}
                vMarginBottom={30}
                vMarginLeft={20}
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
              <nav aria-label={navRegionAriaLabel}>
                <UtilityFragment vGap={8}>
                  <Tabs orientation="vertical">
                    {tabsContent.map(tabContent => (
                      <Tab key={tabContent.id}>
                        <Button colorScheme="tertiary" element={<a href={tabContent.href}>{tabContent.tabLabel}</a>} />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </nav>
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            {navExpanded && (
              <>
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
              </>
            )}
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                iconTwoColor
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
  );
};

```

### Alternate vertical navigation with active element
- **Section**: Default vertical navigations
- **URL**: components/vertical-navigation/alternate-vertical-navigation-with-active-element
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaMediaFastForwardTiny,
  VisaMediaRewindTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
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
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'alternate-vertical-navigation-with-active-element';
const navRegionAriaLabel = 'Alternate vertical navigation with active element';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    active: true,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './vertical-navigation',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const AlternateVerticalNavigationWithActiveElement = () => {
  const [navExpanded, setNavExpanded] = useState(true);
  const [accountTabOpen, setAccountTabOpen] = useState(false);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} alternate orientation="vertical" tag="header">
          {navExpanded && (
            <Link alternate skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <UtilityFragment
                vFlex
                vFlexCol
                vGap={12}
                vMarginTop={16}
                vMarginRight={16}
                vMarginBottom={30}
                vMarginLeft={20}
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
              <nav aria-label={navRegionAriaLabel}>
                <UtilityFragment vGap={8}>
                  <Tabs orientation="vertical">
                    {tabsContent.map(tabContent => (
                      <Tab key={tabContent.id}>
                        <Button
                          aria-current={tabContent.active ? 'page' : false}
                          colorScheme="tertiary"
                          element={<a href={tabContent.href}>{tabContent.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </nav>
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            {navExpanded && (
              <>
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
              </>
            )}
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                iconTwoColor
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
  );
};

```

### Alternate vertical navigation with icons
- **Section**: Default vertical navigations
- **URL**: components/vertical-navigation/alternate-vertical-navigation-with-icons
- **Tags**: 
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaMediaFastForwardTiny,
  VisaMediaRewindTiny,
  VisaStatisticsTiny,
  VisaSettingsTiny,
  VisaSecurityTiny,
  VisaNotesTiny,
  VisaSupportTicketTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
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
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'alternate-vertical-navigation-with-icons';
const navRegionAriaLabel = 'Alternate vertical navigation with icons';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0}`,
    icon: <VisaStatisticsTiny />,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1}`,
    icon: <VisaSettingsTiny />,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2}`,
    icon: <VisaSecurityTiny />,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3}`,
    icon: <VisaNotesTiny />,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4}`,
    icon: <VisaSupportTicketTiny />,
    href: './vertical-navigation',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const AlternateVerticalNavigationWithIcons = () => {
  const [navExpanded, setNavExpanded] = useState(true);
  const [accountTabOpen, setAccountTabOpen] = useState(false);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} alternate orientation="vertical" tag="header">
          {navExpanded && (
            <Link alternate skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <UtilityFragment
                vFlex
                vFlexCol
                vGap={12}
                vMarginTop={16}
                vMarginRight={16}
                vMarginBottom={30}
                vMarginLeft={20}
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
              <nav aria-label={navRegionAriaLabel}>
                <UtilityFragment vGap={8}>
                  <Tabs orientation="vertical">
                    {tabsContent.map(tabContent => (
                      <Tab key={tabContent.id}>
                        <Button
                          colorScheme="tertiary"
                          iconTwoColor
                          element={
                            <a href={tabContent.href}>
                              {tabContent.icon}
                              {tabContent.tabLabel}
                            </a>
                          }
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </nav>
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            {navExpanded && (
              <>
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
              </>
            )}
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
  );
};

```

### Vertical navigation without logo or application name
- **Section**: Custom vertical navigation
- **URL**: components/vertical-navigation/vertical-navigation-without-logo-or-application-name
- **Tags**: 
```tsx
import { VisaMediaFastForwardTiny, VisaMediaRewindTiny } from '@visa/nova-icons-react';
import { Button, Link, Nav, Tab, Tabs, Typography, Utility, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'vertical-navigation-without-logo-or-application-name';
const navRegionAriaLabel = 'Vertical navigation without logo or application name';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const VerticalNavigationWithoutLogoOrApplicationName = () => {
  const [navExpanded, setNavExpanded] = useState(true);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} orientation="vertical" tag="header">
          {navExpanded && (
            <Link skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <nav aria-label={navRegionAriaLabel}>
                <UtilityFragment vGap={8}>
                  <Tabs orientation="vertical">
                    {tabsContent.map(tabContent => (
                      <Tab key={tabContent.id}>
                        <Button colorScheme="tertiary" element={<a href={tabContent.href}>{tabContent.tabLabel}</a>} />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </nav>
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
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

