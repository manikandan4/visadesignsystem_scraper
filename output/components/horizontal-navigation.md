# horizontal-navigation

## Metadata
- **Version**: 0.0.1
- **Description**: Menu or panel at the top of page content that links to important pages or features.
- **Category**: components

## Example Sections
1. **Default horizontal navigations**
   - Description: 
2. **Horizontal navigations with persistent search**
   - Description: 

## Examples
### Default horizontal navigation
- **Section**: Default horizontal navigations
- **URL**: components/horizontal-navigation/default-horizontal-nav
- **Tags**: docs
```tsx
import {
  autoUpdate,
  offset,
  FloatingFocusManager,
  useClick,
  useFloating,
  useInteractions,
  useDismiss,
} from '@floating-ui/react';
import {
  VisaAccountLow,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseLow,
  VisaCloseTiny,
  VisaMenuLow,
  VisaNotificationsLow,
  VisaSearchLow,
} from '@visa/nova-icons-react';
import {
  Avatar,
  Badge,
  Button,
  Divider,
  DropdownButton,
  DropdownMenu,
  Input,
  InputContainer,
  Link,
  Listbox,
  ListboxItem,
  Nav,
  NavAppName,
  Surface,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useEffect, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-horizontal-nav';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './horizontal-navigation',
  },
];

const label3SubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-label-3-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-label-3-sub-item-1`,
    href: './horizontal-navigation',
  },
];

export const DefaultHorizontalNav = () => {
  const searchInputRef = useRef<HTMLInputElement | null>();
  const searchButtonRef = useRef<HTMLButtonElement | null>();

  const [accountMenuOpen, setAccountMenuOpen] = useState(false);
  const [mobileAccountMenuOpen, setMobileAccountMenuOpen] = useState(false);
  const [mobileLabel3MenuOpen, setMobileLabel3MenuOpen] = useState(false);
  const [expandSearch, setExpandSearch] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [label3Open, setLabel3Open] = useState(false);
  const searchInitiallyActivated = useRef(false);

  useEffect(() => {
    if (expandSearch && searchInitiallyActivated.current) {
      searchInputRef.current?.focus();
    }
    if (!expandSearch && searchInitiallyActivated.current) {
      searchButtonRef.current?.focus();
    }
  }, [expandSearch]);
  
  // For dropdown menus in the horizontal nav, we use floating UI for
  // -opening
  // -positioning
  // -dismissing

  // floating-ui setup for the account dropdown
  const {
    context: accountFloatingContext,
    floatingStyles: accountFloatingStyles,
    refs: accountFloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-end',
    whileElementsMounted: autoUpdate,
  });
  const clickAccountRef = useClick(accountFloatingContext);
  const dismissAccountMenu = useDismiss(accountFloatingContext);
  const { getReferenceProps: getAccountReferenceProps, getFloatingProps: getAccountFloatingProps } = useInteractions([
    clickAccountRef,
    dismissAccountMenu,
  ]);

  // floating-ui setup for the label3 tab dropdown
  const {
    context: label3FloatingContext,
    floatingStyles: label3FloatingStyles,
    refs: label3FloatingRefs,
  } = useFloating({
    middleware: [offset(8)],
    open: label3Open,
    onOpenChange: setLabel3Open,
    placement: 'bottom-start',
    whileElementsMounted: autoUpdate,
  });

  const clickLabel3Ref = useClick(label3FloatingContext);
  const dismissLabel3Menu = useDismiss(label3FloatingContext);
  const { getReferenceProps: getLabel3ReferenceProps, getFloatingProps: getLabel3FloatingProps } = useInteractions([
    clickLabel3Ref,
    dismissLabel3Menu,
  ]);

  const onToggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div>
      <Link skipLink href="#content">
        Skip to content
      </Link>
      <UtilityFragment vJustifyContent="between">
        <Nav id={id} orientation="horizontal" tag="header">
          {!expandSearch ? (
            <>
              <UtilityFragment vContainerHide="desktop">
                <DropdownButton
                  aria-controls={`${id}-mobile-menu`}
                  aria-expanded={mobileMenuOpen ? 'true' : 'false'}
                  aria-label="open menu"
                  aria-describedby={`${id}-mobile-menu-notifications-badge`}
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  id={`${id}-mobile-menu-button`}
                  onClick={onToggleMobileMenu}
                >
                  {mobileMenuOpen ? (
                    <VisaCloseTiny />
                  ) : (
                    <>
                      <VisaMenuLow />
                      <Badge
                        id={`${id}-mobile-menu-notifications-badge`}
                        aria-label="3 notifications"
                        badgeVariant="number"
                        tag="sup"
                      >
                        3
                      </Badge>
                    </>
                  )}
                </DropdownButton>
              </UtilityFragment>
              <UtilityFragment vFlex vGap={16}>
                <Link
                  aria-label="Visa Application Name Home"
                  href="./horizontal-navigation"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Utility
                      vContainerHide="xs"
                      element={<Typography variant="headline-3">Application Name</Typography>}
                    />
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <UtilityFragment vFlex vJustifyContent="end" vFlexGrow vMarginLeft="auto" vContainerHide="mobile">
                <nav aria-label="Label for horizontal default example">
                  <UtilityFragment vGap={4}>
                    <Tabs>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 1</a>}
                        />
                      </Tab>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 2</a>}
                        />
                      </Tab>
                      <Tab>
                        <DropdownButton
                          aria-expanded={label3Open}
                          aria-controls={label3Open ? `${id}-label-dropdown-menu` : undefined}
                          id={`${id}-label-dropdown-button`}
                          buttonSize="large"
                          colorScheme="tertiary"
                          ref={label3FloatingRefs.setReference}
                          {...getLabel3ReferenceProps()}
                        >
                          L1 label 3<TabSuffix element={label3Open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                        </DropdownButton>

                        {label3Open && (
                          <FloatingFocusManager
                            context={label3FloatingContext}
                            modal={false}
                            initialFocus={-1}
                            restoreFocus={true}
                          >
                            <DropdownMenu
                              id={`${id}-label-dropdown-menu`}
                              aria-hidden={!label3Open}
                              style={
                                {
                                  inlineSize: '180px',
                                  position: 'absolute',
                                  ...label3FloatingStyles,
                                  zIndex: 1,
                                } as CSSProperties
                              }
                              ref={label3FloatingRefs.setFloating}
                              {...getLabel3FloatingProps()}
                            >
                              <Listbox>
                                {label3SubItems.map(label3SubItem => (
                                  <li key={label3SubItem.id}>
                                    <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                      <ListboxItem href={label3SubItem.href} tag="a">
                                        {label3SubItem.tabLabel}
                                      </ListboxItem>
                                    </UtilityFragment>
                                  </li>
                                ))}
                              </Listbox>
                            </DropdownMenu>
                          </FloatingFocusManager>
                        )}
                      </Tab>
                    </Tabs>
                  </UtilityFragment>
                </nav>
              </UtilityFragment>
              <Utility vFlex vGap={8} vMarginLeft={8}>
                <Button
                  aria-label="search site"
                  buttonSize="large"
                  ref={searchButtonRef}
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => { setExpandSearch(true); searchInitiallyActivated.current = true; }}

                >
                  <VisaSearchLow />
                </Button>
                <UtilityFragment vContainerHide="mobile">
                  <Button
                    aria-label="notifications"
                    aria-describedby={`${id}-notifications-badge`}
                    buttonSize="large"
                    colorScheme="tertiary"
                    iconButton
                  >
                    <VisaNotificationsLow />

                    <Badge id={`${id}-notifications-badge`} badgeVariant="number" tag="sup">
                      3
                    </Badge>
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile">
                  <Tab tag="div">
                    <DropdownButton
                      aria-expanded={accountMenuOpen}
                      aria-controls={accountMenuOpen ? `${id}-account-menu` : undefined}
                      aria-label="Alex Miller"
                      buttonSize="large"
                      colorScheme="tertiary"
                      element={<Avatar tag="button" />}
                      ref={accountFloatingRefs.setReference}
                      {...getAccountReferenceProps()}
                    >
                      <VisaAccountLow />
                      <TabSuffix element={accountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </DropdownButton>
                    {accountMenuOpen && (
                      <FloatingFocusManager
                        context={accountFloatingContext}
                        modal={false}
                        initialFocus={-1}
                        restoreFocus={true}
                      >
                        <DropdownMenu
                          id={`${id}-account-menu`}
                          aria-hidden={!accountMenuOpen}
                          style={
                            {
                              inlineSize: '180px',
                              position: 'absolute',
                              ...accountFloatingStyles,
                              zIndex: 1,
                            } as CSSProperties
                          }
                          ref={accountFloatingRefs.setFloating}
                          {...getAccountFloatingProps()}
                        >
                          <Listbox>
                            {accountSubItems.map(accountSubItem => (
                              <UtilityFragment key={accountSubItem.id}>
                                <li>
                                  <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                    <ListboxItem href={accountSubItem.href} tag="a">
                                      {accountSubItem.tabLabel}
                                    </ListboxItem>
                                  </UtilityFragment>
                                </li>
                              </UtilityFragment>
                            ))}
                          </Listbox>
                        </DropdownMenu>
                      </FloatingFocusManager>
                    )}
                  </Tab>
                </UtilityFragment>
              </Utility>
            </>
          ) : (
            <UtilityFragment vFlex>
              <Surface
                style={
                  {
                    '--v-surface-background': 'var(--palette-default-surface-3)',
                    '--v-surface-border-radius': 'var(--size-rounded-medium)',
                    '--v-surface-padding-inline': 'var(--size-scalable-8)',
                  } as CSSProperties
                }
              >
                <InputContainer>
                  <VisaSearchLow />
                  <Input
                    id={`${id}-search-field`}
                    name={`${id}-search-field`}
                    ref={searchInputRef}
                    required
                    type="search"
                    aria-label="Search"
                    placeholder="Search"
                  />
                </InputContainer>
                <Button
                  aria-label="close search"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => setExpandSearch(false)}
                >
                  <VisaCloseLow />
                </Button>
              </Surface>
            </UtilityFragment>
          )}
        </Nav>
      </UtilityFragment>
      <UtilityFragment vContainerHide="desktop" vHide={!mobileMenuOpen}>
        <Nav
          aria-label="Label for horizontal default example"
          aria-hidden={!mobileMenuOpen}
          id={`${id}-mobile-menu`}
          orientation="vertical"
        >
          <Tabs orientation="vertical">
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 1</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 2</a>}
              />
            </Tab>
            <Tab>
              <Button
                aria-expanded={mobileLabel3MenuOpen}
                aria-controls={mobileLabel3MenuOpen ? `${id}-account-sub-menu` : 'undefined'}
                id={`${id}-mobile-menu-label-dropdown-button`}
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileLabel3MenuOpen(!mobileLabel3MenuOpen)}
              >
                L1 Label 3
                <TabSuffix element={mobileLabel3MenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>

              {mobileLabel3MenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {label3SubItems.map(label3SubItem => (
                    <Tab key={label3SubItem.id} id={label3SubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={label3SubItem.href}>{label3SubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                style={{ wordBreak: 'break-word', blockSize: 'max-content' } as CSSProperties}
              >
                Notifications
                <Badge badgeVariant="number" style={{ position: 'relative' }} tag="sup">
                  3
                </Badge>
              </Button>
            </Tab>
            <Divider dividerType="decorative"></Divider>
            <Tab tag="div">
              <Button
                aria-expanded={mobileAccountMenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                aria-label="Alex Miller"
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileAccountMenuOpen(!mobileAccountMenuOpen)}
              >
                <VisaAccountLow />
                Alex Miller
                <TabSuffix element={mobileAccountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileAccountMenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {accountSubItems.map(accountSubItem => (
                    <Tab key={accountSubItem.id} id={accountSubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
          </Tabs>
        </Nav>
      </UtilityFragment>
    </div>
  );
};

```

### Horizontal navigation with active element
- **Section**: Default horizontal navigations
- **URL**: components/horizontal-navigation/active-element-horizontal-nav
- **Tags**: docs
```tsx
import {
  autoUpdate,
  FloatingFocusManager,
  offset,
  useClick,
  useFloating,
  useInteractions,
  useDismiss,
} from '@floating-ui/react';
import {
  VisaAccountLow,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseLow,
  VisaCloseTiny,
  VisaMenuLow,
  VisaNotificationsLow,
  VisaSearchLow,
} from '@visa/nova-icons-react';
import {
  Avatar,
  Badge,
  Button,
  Divider,
  DropdownButton,
  DropdownMenu,
  Input,
  InputContainer,
  Link,
  Listbox,
  ListboxItem,
  Nav,
  NavAppName,
  Surface,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useEffect, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'active-element-horizontal-nav';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './horizontal-navigation',
  },
];

const label3SubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-label-3-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-label-3-sub-item-1`,
    href: './horizontal-navigation',
  },
];

export const ActiveElementHorizontalNav = () => {
  const searchInputRef = useRef<HTMLInputElement | null>();
  const searchButtonRef = useRef<HTMLButtonElement | null>();

  const [accountMenuOpen, setAccountMenuOpen] = useState(false);
  const [mobileAccountMenuOpen, setMobileAccountMenuOpen] = useState(false);
  const [mobileLabel3MenuOpen, setMobileLabel3MenuOpen] = useState(false);
  const [expandSearch, setExpandSearch] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [label3Open, setLabel3Open] = useState(false);
  const searchInitiallyActivated = useRef(false);

  useEffect(() => {
    if (expandSearch && searchInitiallyActivated.current) {
      searchInputRef.current?.focus();
    }
    if (!expandSearch && searchInitiallyActivated.current) {
      searchButtonRef.current?.focus();
    }
  }, [expandSearch]);

  // For dropdown menus in the horizontal nav, we use floating UI for
  // -opening
  // -positioning
  // -dismissing

  // floating-ui setup for the account dropdown
  const {
    context: accountFloatingContext,
    floatingStyles: accountFloatingStyles,
    refs: accountFloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-end',
    whileElementsMounted: autoUpdate,
  });
  const clickAccountRef = useClick(accountFloatingContext);
  const dismissAccountMenu = useDismiss(accountFloatingContext);
  const { getReferenceProps: getAccountReferenceProps, getFloatingProps: getAccountFloatingProps } = useInteractions([
    clickAccountRef,
    dismissAccountMenu,
  ]);

  // floating-ui setup for the label3 tab dropdown
  const {
    context: label3FloatingContext,
    floatingStyles: label3FloatingStyles,
    refs: label3FloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: label3Open,
    onOpenChange: setLabel3Open,
    placement: 'bottom-start',
    whileElementsMounted: autoUpdate,
  });
  const clickLabel3Ref = useClick(label3FloatingContext);
  const dismissLabel3Menu = useDismiss(label3FloatingContext);
  const { getReferenceProps: getLabel3ReferenceProps, getFloatingProps: getLabel3FloatingProps } = useInteractions([
    clickLabel3Ref,
    dismissLabel3Menu,
  ]);

  const onToggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div>
      <Link skipLink href="#content">
        Skip to content
      </Link>
      <UtilityFragment vJustifyContent="between">
        <Nav id={id} orientation="horizontal" tag="header">
          {!expandSearch ? (
            <>
              <UtilityFragment vContainerHide="desktop">
                <DropdownButton
                  aria-controls={`${id}-mobile-menu`}
                  aria-expanded={mobileMenuOpen ? 'true' : 'false'}
                  aria-describedby={`${id}-mobile-menu-notifications-badge`}
                  aria-label="open menu"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  id={`${id}-mobile-menu-button`}
                  onClick={onToggleMobileMenu}
                >
                  {mobileMenuOpen ? (
                    <VisaCloseTiny />
                  ) : (
                    <>
                      <VisaMenuLow />
                      <Badge
                        id={`${id}-mobile-menu-notifications-badge`}
                        aria-label="3 notifications"
                        badgeVariant="number"
                        tag="sup"
                      >
                        3
                      </Badge>
                    </>
                  )}
                </DropdownButton>
              </UtilityFragment>
              <UtilityFragment vFlex vGap={16}>
                <Link
                  aria-label="Visa Application Name Home"
                  href="./horizontal-navigation"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Utility
                      vContainerHide="xs"
                      element={<Typography variant="headline-3">Application Name</Typography>}
                    />
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <UtilityFragment vFlex vJustifyContent="end" vFlexGrow vMarginLeft="auto" vContainerHide="mobile">
                <nav aria-label="Label for horizontal example with active element">
                  <UtilityFragment vGap={4}>
                    <Tabs>
                      <Tab>
                        <Button
                          aria-current="page"
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 1</a>}
                        />
                      </Tab>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 2</a>}
                        />
                      </Tab>
                      <Tab>
                        <DropdownButton
                          aria-expanded={label3Open}
                          aria-controls={label3Open ? `${id}-label-dropdown-menu` : undefined}
                          id={`${id}-label-dropdown-button`}
                          buttonSize="large"
                          colorScheme="tertiary"
                          ref={label3FloatingRefs.setReference}
                          {...getLabel3ReferenceProps()}
                        >
                          L1 label 3<TabSuffix element={label3Open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                        </DropdownButton>
                        {label3Open && (
                          <FloatingFocusManager
                            context={label3FloatingContext}
                            modal={false}
                            initialFocus={-1}
                            restoreFocus={true}
                          >
                            <DropdownMenu
                              id={`${id}-label-dropdown-menu`}
                              aria-hidden={!label3Open}
                              style={
                                {
                                  inlineSize: '180px',
                                  position: 'absolute',
                                  ...label3FloatingStyles,
                                  zIndex: 1,
                                } as CSSProperties
                              }
                              ref={label3FloatingRefs.setFloating}
                              {...getLabel3FloatingProps()}
                            >
                              <Listbox>
                                {label3SubItems.map(label3SubItem => (
                                  <li key={label3SubItem.id}>
                                    <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                      <ListboxItem href={label3SubItem.href} tag="a">
                                        {label3SubItem.tabLabel}
                                      </ListboxItem>
                                    </UtilityFragment>
                                  </li>
                                ))}
                              </Listbox>
                            </DropdownMenu>
                          </FloatingFocusManager>
                        )}
                      </Tab>
                    </Tabs>
                  </UtilityFragment>
                </nav>
              </UtilityFragment>
              <Utility vFlex vGap={8} vMarginLeft={8}>
                <Button
                  aria-label="search site"
                  buttonSize="large"
                  ref={searchButtonRef}
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => { setExpandSearch(true); searchInitiallyActivated.current = true; }}
                >
                  <VisaSearchLow />
                </Button>
                <UtilityFragment vContainerHide="mobile">
                  <Button
                    aria-label="notifications"
                    aria-describedby={`${id}-notifications-badge`}
                    buttonSize="large"
                    colorScheme="tertiary"
                    iconButton
                  >
                    <VisaNotificationsLow />
                    <Badge id={`${id}-notifications-badge`} badgeVariant="number" tag="sup">
                      3
                    </Badge>
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile">
                  <Tab tag="div">
                    <DropdownButton
                      aria-expanded={accountMenuOpen}
                      aria-controls={accountMenuOpen ? `${id}-account-menu` : undefined}
                      aria-label="Alex Miller"
                      buttonSize="large"
                      colorScheme="tertiary"
                      element={<Avatar tag="button" />}
                      ref={accountFloatingRefs.setReference}
                      {...getAccountReferenceProps()}
                    >
                      <VisaAccountLow />
                      <TabSuffix element={accountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </DropdownButton>
                    {accountMenuOpen && (
                      <FloatingFocusManager
                        context={accountFloatingContext}
                        modal={false}
                        initialFocus={-1}
                        restoreFocus={true}
                      >
                        <DropdownMenu
                          id={`${id}-account-menu`}
                          aria-hidden={!accountMenuOpen}
                          style={
                            {
                              inlineSize: '180px',
                              position: 'absolute',
                              ...accountFloatingStyles,
                              zIndex: 1,
                            } as CSSProperties
                          }
                          ref={accountFloatingRefs.setFloating}
                          {...getAccountFloatingProps()}
                        >
                          <Listbox>
                            {accountSubItems.map(accountSubItem => (
                              <UtilityFragment key={accountSubItem.id}>
                                <li>
                                  <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                    <ListboxItem href={accountSubItem.href} tag="a">
                                      {accountSubItem.tabLabel}
                                    </ListboxItem>
                                  </UtilityFragment>
                                </li>
                              </UtilityFragment>
                            ))}
                          </Listbox>
                        </DropdownMenu>
                      </FloatingFocusManager>
                    )}
                  </Tab>
                </UtilityFragment>
              </Utility>
            </>
          ) : (
            <UtilityFragment vFlex>
              <Surface
                style={
                  {
                    '--v-surface-background': 'var(--palette-default-surface-3)',
                    '--v-surface-border-radius': 'var(--size-rounded-medium)',
                    '--v-surface-padding-inline': 'var(--size-scalable-8)',
                  } as CSSProperties
                }
              >
                <InputContainer>
                  <VisaSearchLow />
                  <Input
                    id={`${id}-search-field`}
                    name={`${id}-search-field`}
                    ref={searchInputRef}
                    required
                    type="search"
                    aria-label="Search"
                    placeholder="Search"
                  />
                </InputContainer>
                <Button
                  aria-label="close search"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => setExpandSearch(false)}
                >
                  <VisaCloseLow />
                </Button>
              </Surface>
            </UtilityFragment>
          )}
        </Nav>
      </UtilityFragment>
      <UtilityFragment vContainerHide="desktop" vHide={!mobileMenuOpen}>
        <Nav
          aria-label="Label for horizontal example with active element"
          aria-hidden={!mobileMenuOpen}
          id={`${id}-mobile-menu`}
          orientation="vertical"
        >
          <Tabs orientation="vertical">
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 1</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 2</a>}
              />
            </Tab>

            <Tab tag="div">
              <Button
                aria-expanded={mobileLabel3MenuOpen}
                aria-controls={mobileLabel3MenuOpen ? `${id}-account-sub-menu` : 'undefined'}
                id={`${id}-mobile-menu-label-dropdown-button`}
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileLabel3MenuOpen(!mobileLabel3MenuOpen)}
              >
                L1 Label 3
                <TabSuffix element={mobileLabel3MenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>

              {mobileLabel3MenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {label3SubItems.map(label3SubItem => (
                    <Tab key={label3SubItem.id} id={label3SubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={label3SubItem.href}>{label3SubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                style={{ wordBreak: 'break-word', blockSize: 'max-content' } as CSSProperties}
              >
                Notifications
                <Badge badgeVariant="number" style={{ position: 'relative' }} tag="sup">
                  3
                </Badge>
              </Button>
            </Tab>
            <Divider dividerType="decorative"></Divider>
            <Tab tag="div">
              <Button
                aria-expanded={mobileAccountMenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                aria-label="Alex Miller"
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileAccountMenuOpen(!mobileAccountMenuOpen)}
              >
                <VisaAccountLow />
                Alex Miller
                <TabSuffix element={mobileAccountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileAccountMenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {accountSubItems.map(accountSubItem => (
                    <Tab key={accountSubItem.id} id={accountSubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
          </Tabs>
        </Nav>
      </UtilityFragment>
    </div>
  );
};

```

### Horizontal navigation with icons
- **Section**: Default horizontal navigations
- **URL**: components/horizontal-navigation/horizontal-with-icons
- **Tags**: custom
```tsx
import {
  autoUpdate,
  FloatingFocusManager,
  offset,
  useClick,
  useFloating,
  useInteractions,
  useDismiss,
} from '@floating-ui/react';

import {
  VisaAccountLow,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseLow,
  VisaCloseTiny,
  VisaMenuLow,
  VisaNotificationsLow,
  VisaSearchLow,
  VisaSecurityTiny,
  VisaSettingsTiny,
  VisaStatisticsTiny,
} from '@visa/nova-icons-react';
import {
  Avatar,
  Badge,
  Button,
  Divider,
  DropdownButton,
  DropdownMenu,
  Input,
  InputContainer,
  Link,
  Listbox,
  ListboxItem,
  Nav,
  NavAppName,
  Surface,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useEffect, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-horizontal-nav';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './horizontal-navigation',
  },
];

const label3SubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-label-3-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-label-3-sub-item-1`,
    href: './horizontal-navigation',
  },
];

export const DefaultHorizontalNav = () => {
  const searchInputRef = useRef<HTMLInputElement | null>();
  const searchButtonRef = useRef<HTMLButtonElement | null>();

  const [accountMenuOpen, setAccountMenuOpen] = useState(false);
  const [mobileAccountMenuOpen, setMobileAccountMenuOpen] = useState(false);
  const [mobileLabel3MenuOpen, setMobileLabel3MenuOpen] = useState(false);
  const [expandSearch, setExpandSearch] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [label3Open, setLabel3Open] = useState(false);
  const searchInitiallyActivated = useRef(false);

  useEffect(() => {
    if (expandSearch && searchInitiallyActivated.current) {
      searchInputRef.current?.focus();
    }
    if (!expandSearch && searchInitiallyActivated.current) {
      searchButtonRef.current?.focus();
    }
  }, [expandSearch]);

  // For dropdown menus in the horizontal nav, we use floating UI for
  // -opening
  // -positioning
  // -dismissing

  // floating-ui setup for the account dropdown
  const {
    context: accountFloatingContext,
    floatingStyles: accountFloatingStyles,
    refs: accountFloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-end',
    whileElementsMounted: autoUpdate,
  });
  const clickAccountRef = useClick(accountFloatingContext);
  const dismissAccountMenu = useDismiss(accountFloatingContext);
  const { getReferenceProps: getAccountReferenceProps, getFloatingProps: getAccountFloatingProps } = useInteractions([
    clickAccountRef,
    dismissAccountMenu,
  ]);

  // floating-ui setup for the label3 tab dropdown
  const {
    context: label3FloatingContext,
    floatingStyles: label3FloatingStyles,
    refs: label3FloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: label3Open,
    onOpenChange: setLabel3Open,
    placement: 'bottom-start',
    whileElementsMounted: autoUpdate,
  });
  const clickLabel3Ref = useClick(label3FloatingContext);
  const dismissLabel3Menu = useDismiss(label3FloatingContext);
  const { getReferenceProps: getLabel3ReferenceProps, getFloatingProps: getLabel3FloatingProps } = useInteractions([
    clickLabel3Ref,
    dismissLabel3Menu,
  ]);

  const onToggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div>
      <Link skipLink href="#content">
        Skip to content
      </Link>
      <UtilityFragment vJustifyContent="between">
        <Nav orientation="horizontal" tag="header">
          {!expandSearch ? (
            <>
              <UtilityFragment vContainerHide="desktop">
                <DropdownButton
                  aria-controls={`${id}-mobile-menu`}
                  aria-expanded={mobileMenuOpen ? 'true' : 'false'}
                  aria-describedby={`${id}-mobile-menu-notifications-badge`}
                  aria-label="open menu"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  id={`${id}-mobile-menu-button`}
                  onClick={onToggleMobileMenu}
                >
                  {mobileMenuOpen ? (
                    <VisaCloseTiny />
                  ) : (
                    <>
                      <VisaMenuLow />
                      <Badge
                        id={`${id}-mobile-menu-notifications-badge`}
                        aria-label="3 notifications"
                        badgeVariant="number"
                        tag="sup"
                      >
                        3
                      </Badge>
                    </>
                  )}
                </DropdownButton>
              </UtilityFragment>
              <UtilityFragment vFlex vGap={16}>
                <Link
                  aria-label="Visa Application Name Home"
                  href="./horizontal-navigation"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Utility
                      vContainerHide="xs"
                      element={<Typography variant="headline-3">Application Name</Typography>}
                    />
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <UtilityFragment vFlex vJustifyContent="end" vFlexGrow vMarginLeft="auto" vContainerHide="mobile">
                <nav aria-label="Label for horizontal example with icons">
                  <UtilityFragment vGap={4}>
                    <Tabs>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">{<VisaStatisticsTiny />}L1 label 1</a>}
                        />
                      </Tab>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">{<VisaSettingsTiny />}L1 label 2</a>}
                        />
                      </Tab>
                      <Tab>
                        <DropdownButton
                          aria-expanded={label3Open}
                          aria-controls={label3Open ? `${id}-label-dropdown-menu` : undefined}
                          id={`${id}-label-dropdown-button`}
                          buttonSize="large"
                          colorScheme="tertiary"
                          ref={label3FloatingRefs.setReference}
                          {...getLabel3ReferenceProps()}
                        >
                          <VisaSecurityTiny />
                          L1 label 3<TabSuffix element={label3Open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                        </DropdownButton>

                        {label3Open && (
                          <FloatingFocusManager
                            context={label3FloatingContext}
                            modal={false}
                            initialFocus={-1}
                            restoreFocus={true}
                          >
                            <DropdownMenu
                              id={`${id}-label-dropdown-menu`}
                              aria-hidden={!label3Open}
                              style={
                                {
                                  inlineSize: '180px',
                                  position: 'absolute',
                                  ...label3FloatingStyles,
                                  zIndex: 1,
                                } as CSSProperties
                              }
                              ref={label3FloatingRefs.setFloating}
                              {...getLabel3FloatingProps()}
                            >
                              <Listbox>
                                {label3SubItems.map(label3SubItem => (
                                  <li key={label3SubItem.id}>
                                    <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                      <ListboxItem href={label3SubItem.href} tag="a">
                                        {label3SubItem.tabLabel}
                                      </ListboxItem>
                                    </UtilityFragment>
                                  </li>
                                ))}
                              </Listbox>
                            </DropdownMenu>
                          </FloatingFocusManager>
                        )}
                      </Tab>
                    </Tabs>
                  </UtilityFragment>
                </nav>
              </UtilityFragment>
              <Utility vFlex vGap={8} vMarginLeft={8}>
                <Button
                  aria-label="search site"
                  buttonSize="large"
                  ref={searchButtonRef}
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => { setExpandSearch(true); searchInitiallyActivated.current = true; }}
                >
                  <VisaSearchLow />
                </Button>
                <UtilityFragment vContainerHide="mobile">
                  <Button
                    aria-describedby={`${id}-notifications-badge`}
                    aria-label="notifications"
                    buttonSize="large"
                    colorScheme="tertiary"
                    iconButton
                  >
                    <VisaNotificationsLow />
                    <Badge id={`${id}-notifications-badge`} badgeVariant="number" tag="sup">
                      3
                    </Badge>
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile">
                  <Tab tag="div">
                    <DropdownButton
                      aria-expanded={accountMenuOpen}
                      aria-controls={accountMenuOpen ? `${id}-account-menu` : undefined}
                      aria-label="Alex Miller"
                      buttonSize="large"
                      colorScheme="tertiary"
                      element={<Avatar tag="button" />}
                      ref={accountFloatingRefs.setReference}
                      {...getAccountReferenceProps()}
                    >
                      <VisaAccountLow />
                      <TabSuffix element={accountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </DropdownButton>
                    {accountMenuOpen && (
                      <FloatingFocusManager
                        context={accountFloatingContext}
                        modal={false}
                        initialFocus={-1}
                        restoreFocus={true}
                      >
                        <DropdownMenu
                          id={`${id}-account-menu`}
                          aria-hidden={!accountMenuOpen}
                          style={
                            {
                              inlineSize: '180px',
                              position: 'absolute',
                              ...accountFloatingStyles,
                              zIndex: 1,
                            } as CSSProperties
                          }
                          ref={accountFloatingRefs.setFloating}
                          {...getAccountFloatingProps()}
                        >
                          <Listbox>
                            {accountSubItems.map(accountSubItem => (
                              <UtilityFragment key={accountSubItem.id}>
                                <li>
                                  <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                    <ListboxItem href={accountSubItem.href} tag="a">
                                      {accountSubItem.tabLabel}
                                    </ListboxItem>
                                  </UtilityFragment>
                                </li>
                              </UtilityFragment>
                            ))}
                          </Listbox>
                        </DropdownMenu>
                      </FloatingFocusManager>
                    )}
                  </Tab>
                </UtilityFragment>
              </Utility>
            </>
          ) : (
            <UtilityFragment vFlex>
              <Surface
                style={
                  {
                    '--v-surface-background': 'var(--palette-default-surface-3)',
                    '--v-surface-border-radius': 'var(--size-rounded-medium)',
                    '--v-surface-padding-inline': 'var(--size-scalable-8)',
                  } as CSSProperties
                }
              >
                <InputContainer>
                  <VisaSearchLow />
                  <Input
                    id={`${id}-search-field`}
                    name={`${id}-search-field`}
                    ref={searchInputRef}
                    required
                    type="search"
                    aria-label="Search"
                    placeholder="Search"
                  />
                </InputContainer>
                <Button
                  aria-label="close search"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => setExpandSearch(false)}
                >
                  <VisaCloseLow />
                </Button>
              </Surface>
            </UtilityFragment>
          )}
        </Nav>
      </UtilityFragment>
      <UtilityFragment vContainerHide="desktop" vHide={!mobileMenuOpen}>
        <Nav
          aria-label="Label for horizontal example with icons"
          aria-hidden={!mobileMenuOpen}
          id={`${id}-mobile-menu`}
          orientation="vertical"
        >
          <Tabs orientation="vertical">
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 1</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 2</a>}
              />
            </Tab>
            <Tab>
              <Button
                aria-expanded={mobileLabel3MenuOpen}
                aria-controls={mobileLabel3MenuOpen ? `${id}-account-sub-menu` : 'undefined'}
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileLabel3MenuOpen(!mobileLabel3MenuOpen)}
              >
                L1 Label 3
                <TabSuffix element={mobileLabel3MenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>

              {mobileLabel3MenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {label3SubItems.map(label3SubItem => (
                    <Tab key={label3SubItem.id} id={label3SubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={label3SubItem.href}>{label3SubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                style={{ wordBreak: 'break-word', blockSize: 'max-content' } as CSSProperties}
              >
                Notifications
                <Badge badgeVariant="number" style={{ position: 'relative' }} tag="sup">
                  3
                </Badge>
              </Button>
            </Tab>
            <Divider dividerType="decorative"></Divider>
            <Tab tag="div">
              <Button
                aria-expanded={mobileAccountMenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                aria-label="Alex Miller"
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileAccountMenuOpen(!mobileAccountMenuOpen)}
              >
                <VisaAccountLow />
                Alex Miller
                <TabSuffix element={mobileAccountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileAccountMenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {accountSubItems.map(accountSubItem => (
                    <Tab key={accountSubItem.id} id={accountSubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
          </Tabs>
        </Nav>
      </UtilityFragment>
    </div>
  );
};

```

### Alternate horizontal navigation
- **Section**: Default horizontal navigations
- **URL**: components/horizontal-navigation/alternate-horizontal-nav
- **Tags**: docs
```tsx
import {
  autoUpdate,
  FloatingFocusManager,
  offset,
  useClick,
  useFloating,
  useInteractions,
  useDismiss,
} from '@floating-ui/react';
import {
  VisaAccountLow,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseLow,
  VisaCloseTiny,
  VisaMenuLow,
  VisaNotificationsLow,
  VisaSearchLow,
} from '@visa/nova-icons-react';
import {
  Avatar,
  Badge,
  Button,
  Divider,
  DropdownButton,
  DropdownMenu,
  Input,
  InputContainer,
  Link,
  Listbox,
  ListboxItem,
  Nav,
  NavAppName,
  Surface,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useEffect, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'alternate-horizontal-nav';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './horizontal-navigation',
  },
];

const label3SubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-label-3-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-label-3-sub-item-1`,
    href: './horizontal-navigation',
  },
];

export const AlternateHorizontalNav = () => {
  const searchInputRef = useRef<HTMLInputElement | null>();
  const searchButtonRef = useRef<HTMLButtonElement | null>();

  const [accountMenuOpen, setAccountMenuOpen] = useState(false);
  const [mobileAccountMenuOpen, setMobileAccountMenuOpen] = useState(false);
  const [mobileLabel3MenuOpen, setMobileLabel3MenuOpen] = useState(false);
  const [expandSearch, setExpandSearch] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [label3Open, setLabel3Open] = useState(false);
  const searchInitiallyActivated = useRef(false);

  useEffect(() => {
    if (expandSearch && searchInitiallyActivated.current) {
      searchInputRef.current?.focus();
    }
    if (!expandSearch && searchInitiallyActivated.current) {
      searchButtonRef.current?.focus();
    }
  }, [expandSearch]);

  // For dropdown menus in the horizontal nav, we use floating UI for
  // -opening
  // -positioning
  // -dismissing

  // floating-ui setup for the account dropdown
  const {
    context: accountFloatingContext,
    floatingStyles: accountFloatingStyles,
    refs: accountFloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-end',
    whileElementsMounted: autoUpdate,
  });
  const clickAccountRef = useClick(accountFloatingContext);
  const dismissAccountMenu = useDismiss(accountFloatingContext);
  const { getReferenceProps: getAccountReferenceProps, getFloatingProps: getAccountFloatingProps } = useInteractions([
    clickAccountRef,
    dismissAccountMenu,
  ]);

  // floating-ui setup for the label3 tab dropdown
  const {
    context: label3FloatingContext,
    floatingStyles: label3FloatingStyles,
    refs: label3FloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: label3Open,
    onOpenChange: setLabel3Open,
    placement: 'bottom-start',
    whileElementsMounted: autoUpdate,
  });
  const clickLabel3Ref = useClick(label3FloatingContext);
  const dismissLabel3Menu = useDismiss(label3FloatingContext);
  const { getReferenceProps: getLabel3ReferenceProps, getFloatingProps: getLabel3FloatingProps } = useInteractions([
    clickLabel3Ref,
    dismissLabel3Menu,
  ]);

  const onToggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div>
      <Link alternate skipLink href="#content">
        Skip to content
      </Link>
      <UtilityFragment vJustifyContent="between">
        <Nav id={id} alternate orientation="horizontal" tag="header">
          {!expandSearch ? (
            <>
              <UtilityFragment vContainerHide="desktop">
                <DropdownButton
                  aria-controls={`${id}-mobile-menu`}
                  aria-expanded={mobileMenuOpen ? 'true' : 'false'}
                  aria-describedby={`${id}-mobile-menu-notifications-badge`}
                  aria-label="open menu"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  id={`${id}-mobile-menu-button`}
                  onClick={onToggleMobileMenu}
                >
                  {mobileMenuOpen ? (
                    <VisaCloseTiny />
                  ) : (
                    <>
                      <VisaMenuLow />
                      <Badge
                        id={`${id}-mobile-menu-notifications-badge`}
                        aria-label="3 notifications"
                        badgeVariant="number"
                        tag="sup"
                      >
                        3
                      </Badge>
                    </>
                  )}
                </DropdownButton>
              </UtilityFragment>
              <UtilityFragment vFlex vGap={16}>
                <Link
                  aria-label="Visa Application Name Home"
                  href="./horizontal-navigation"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Utility
                      vContainerHide="xs"
                      element={<Typography variant="headline-3">Application Name</Typography>}
                    />
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <UtilityFragment vFlex vJustifyContent="end" vFlexGrow vMarginLeft="auto" vContainerHide="mobile">
                <nav aria-label="Label for alternate horizontal example">
                  <UtilityFragment vGap={4}>
                    <Tabs>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 1</a>}
                        />
                      </Tab>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 2</a>}
                        />
                      </Tab>
                      <Tab>
                        <DropdownButton
                          aria-expanded={label3Open}
                          aria-controls={label3Open ? `${id}-label-dropdown-menu` : undefined}
                          id={`${id}-label-dropdown-button`}
                          buttonSize="large"
                          colorScheme="tertiary"
                          ref={label3FloatingRefs.setReference}
                          {...getLabel3ReferenceProps()}
                        >
                          L1 label 3<TabSuffix element={label3Open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                        </DropdownButton>

                        {label3Open && (
                          <FloatingFocusManager
                            context={label3FloatingContext}
                            modal={false}
                            initialFocus={-1}
                            restoreFocus={true}
                          >
                            <DropdownMenu
                              id={`${id}-label-dropdown-menu`}
                              aria-hidden={!label3Open}
                              style={
                                {
                                  inlineSize: '180px',
                                  position: 'absolute',
                                  ...label3FloatingStyles,
                                  zIndex: 1,
                                } as CSSProperties
                              }
                              ref={label3FloatingRefs.setFloating}
                              {...getLabel3FloatingProps()}
                            >
                              <Listbox>
                                {label3SubItems.map(label3SubItem => (
                                  <li key={label3SubItem.id}>
                                    <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                      <ListboxItem href={label3SubItem.href} tag="a">
                                        {label3SubItem.tabLabel}
                                      </ListboxItem>
                                    </UtilityFragment>
                                  </li>
                                ))}
                              </Listbox>
                            </DropdownMenu>
                          </FloatingFocusManager>
                        )}
                      </Tab>
                    </Tabs>
                  </UtilityFragment>
                </nav>
              </UtilityFragment>
              <Utility vFlex vGap={8} vMarginLeft={8}>
                <Button
                  aria-label="search site"
                  ref={searchButtonRef}
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => { setExpandSearch(true); searchInitiallyActivated.current = true; }}
                >
                  <VisaSearchLow />
                </Button>
                <UtilityFragment vContainerHide="mobile">
                  <Button
                    aria-label="notifications"
                    aria-describedby={`${id}-notifications-badge`}
                    buttonSize="large"
                    colorScheme="tertiary"
                    iconButton
                  >
                    <VisaNotificationsLow />
                    <Badge id={`${id}-notifications-badge`} badgeVariant="number" tag="sup">
                      3
                    </Badge>
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile">
                  <Tab tag="div">
                    <DropdownButton
                      aria-expanded={accountMenuOpen}
                      aria-controls={accountMenuOpen ? `${id}-account-menu` : undefined}
                      aria-label="Alex Miller"
                      buttonSize="large"
                      colorScheme="tertiary"
                      element={<Avatar tag="button" />}
                      ref={accountFloatingRefs.setReference}
                      {...getAccountReferenceProps()}
                    >
                      <VisaAccountLow />
                      <TabSuffix element={accountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </DropdownButton>
                    {accountMenuOpen && (
                      <FloatingFocusManager
                        context={accountFloatingContext}
                        modal={false}
                        initialFocus={-1}
                        restoreFocus={true}
                      >
                        <DropdownMenu
                          id={`${id}-account-menu`}
                          aria-hidden={!accountMenuOpen}
                          style={
                            {
                              inlineSize: '180px',
                              position: 'absolute',
                              ...accountFloatingStyles,
                              zIndex: 1,
                            } as CSSProperties
                          }
                          ref={accountFloatingRefs.setFloating}
                          {...getAccountFloatingProps()}
                        >
                          <Listbox>
                            {accountSubItems.map(accountSubItem => (
                              <UtilityFragment key={accountSubItem.id}>
                                <li>
                                  <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                    <ListboxItem href={accountSubItem.href} tag="a">
                                      {accountSubItem.tabLabel}
                                    </ListboxItem>
                                  </UtilityFragment>
                                </li>
                              </UtilityFragment>
                            ))}
                          </Listbox>
                        </DropdownMenu>
                      </FloatingFocusManager>
                    )}
                  </Tab>
                </UtilityFragment>
              </Utility>
            </>
          ) : (
            <UtilityFragment vFlex>
              <Surface
                style={
                  {
                    '--v-surface-background': 'var(--palette-default-surface-3)',
                    '--v-surface-border-radius': 'var(--size-rounded-medium)',
                    '--v-surface-padding-inline': 'var(--size-scalable-8)',
                  } as CSSProperties
                }
              >
                <InputContainer>
                  <VisaSearchLow />
                  <Input
                    id={`${id}-search-field`}
                    name={`${id}-search-field`}
                    ref={searchInputRef}
                    required
                    type="search"
                    aria-label="Search"
                    placeholder="Search"
                  />
                </InputContainer>
                <Button
                  aria-label="close search"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => setExpandSearch(false)}
                >
                  <VisaCloseLow />
                </Button>
              </Surface>
            </UtilityFragment>
          )}
        </Nav>
      </UtilityFragment>
      <UtilityFragment vContainerHide="desktop" vHide={!mobileMenuOpen}>
        <Nav
          alternate
          aria-label="Label for alternate horizontal example"
          aria-hidden={!mobileMenuOpen}
          id={`${id}-mobile-menu`}
          orientation="vertical"
        >
          <Tabs orientation="vertical">
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 1</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 2</a>}
              />
            </Tab>
            <Tab>
              <Button
                aria-expanded={mobileLabel3MenuOpen}
                aria-controls={mobileLabel3MenuOpen ? `${id}-account-sub-menu` : 'undefined'}
                id={`${id}-mobile-menu-label-dropdown-button`}
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileLabel3MenuOpen(!mobileLabel3MenuOpen)}
              >
                L1 Label 3
                <TabSuffix element={mobileLabel3MenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>

              {mobileLabel3MenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {label3SubItems.map(label3SubItem => (
                    <Tab key={label3SubItem.id} id={label3SubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={label3SubItem.href}>{label3SubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                style={{ wordBreak: 'break-word', blockSize: 'max-content' } as CSSProperties}
              >
                Notifications
                <Badge
                  badgeVariant="number"
                  style={
                    {
                      position: 'relative',
                    } as CSSProperties
                  }
                  tag="sup"
                >
                  3
                </Badge>
              </Button>
            </Tab>
            <Divider dividerType="decorative"></Divider>
            <Tab tag="div">
              <Button
                aria-expanded={mobileAccountMenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                aria-label="Alex Miller"
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileAccountMenuOpen(!mobileAccountMenuOpen)}
              >
                <VisaAccountLow />
                Alex Miller
                <TabSuffix element={mobileAccountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileAccountMenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {accountSubItems.map(accountSubItem => (
                    <Tab key={accountSubItem.id} id={accountSubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
          </Tabs>
        </Nav>
      </UtilityFragment>
    </div>
  );
};

```

### Alternate horizontal navigation with active element
- **Section**: Default horizontal navigations
- **URL**: components/horizontal-navigation/alternate-active-element-horizontal-nav
- **Tags**: docs
```tsx
import {
  autoUpdate,
  FloatingFocusManager,
  offset,
  useClick,
  useFloating,
  useInteractions,
  useDismiss,
} from '@floating-ui/react';
import {
  VisaAccountLow,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseLow,
  VisaCloseTiny,
  VisaMenuLow,
  VisaNotificationsLow,
  VisaSearchLow,
} from '@visa/nova-icons-react';
import {
  Avatar,
  Badge,
  Button,
  Divider,
  DropdownButton,
  DropdownMenu,
  Input,
  InputContainer,
  Link,
  Listbox,
  ListboxItem,
  Nav,
  NavAppName,
  Surface,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useEffect, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'alternate-active-element-horizontal-nav';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './horizontal-navigation',
  },
];

const label3SubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-label-3-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-label-3-sub-item-1`,
    href: './horizontal-navigation',
  },
];

export const AlternateActiveElementHorizontalNav = () => {
  const searchInputRef = useRef<HTMLInputElement | null>();
  const searchButtonRef = useRef<HTMLButtonElement | null>();

  const [accountMenuOpen, setAccountMenuOpen] = useState(false);
  const [mobileAccountMenuOpen, setMobileAccountMenuOpen] = useState(false);
  const [mobileLabel3MenuOpen, setMobileLabel3MenuOpen] = useState(false);
  const [expandSearch, setExpandSearch] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [label3Open, setLabel3Open] = useState(false);
  const searchInitiallyActivated = useRef(false);

  useEffect(() => {
    if (expandSearch && searchInitiallyActivated.current) {
      searchInputRef.current?.focus();
    }
    if (!expandSearch && searchInitiallyActivated.current) {
      searchButtonRef.current?.focus();
    }
  }, [expandSearch]);

  // For dropdown menus in the horizontal nav, we use floating UI for
  // -opening
  // -positioning
  // -dismissing

  // floating-ui setup for the account dropdown
  const {
    context: accountFloatingContext,
    floatingStyles: accountFloatingStyles,
    refs: accountFloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-end',
    whileElementsMounted: autoUpdate,
  });
  const clickAccountRef = useClick(accountFloatingContext);
  const dismissAccountMenu = useDismiss(accountFloatingContext);
  const { getReferenceProps: getAccountReferenceProps, getFloatingProps: getAccountFloatingProps } = useInteractions([
    clickAccountRef,
    dismissAccountMenu,
  ]);

  // floating-ui setup for the label3 tab dropdown
  const {
    context: label3FloatingContext,
    floatingStyles: label3FloatingStyles,
    refs: label3FloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: label3Open,
    onOpenChange: setLabel3Open,
    placement: 'bottom-start',
    whileElementsMounted: autoUpdate,
  });
  const clickLabel3Ref = useClick(label3FloatingContext);
  const dismissLabel3Menu = useDismiss(label3FloatingContext);
  const { getReferenceProps: getLabel3ReferenceProps, getFloatingProps: getLabel3FloatingProps } = useInteractions([
    clickLabel3Ref,
    dismissLabel3Menu,
  ]);

  const onToggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div>
      <Link alternate skipLink href="#content">
        Skip to content
      </Link>
      <UtilityFragment vJustifyContent="between">
        <Nav id={id} alternate orientation="horizontal" tag="header">
          {!expandSearch ? (
            <>
              <UtilityFragment vContainerHide="desktop">
                <DropdownButton
                  aria-controls={`${id}-mobile-menu`}
                  aria-expanded={mobileMenuOpen ? 'true' : 'false'}
                  aria-describedby={`${id}-mobile-menu-notifications-badge`}
                  aria-label="open menu"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  id={`${id}-mobile-menu-button`}
                  onClick={onToggleMobileMenu}
                >
                  {mobileMenuOpen ? (
                    <VisaCloseTiny />
                  ) : (
                    <>
                      <VisaMenuLow />
                      <Badge
                        id={`${id}-mobile-menu-notifications-badge`}
                        aria-label="3 notifications"
                        badgeVariant="number"
                        tag="sup"
                      >
                        3
                      </Badge>
                    </>
                  )}
                </DropdownButton>
              </UtilityFragment>
              <UtilityFragment vFlex vGap={16}>
                <Link
                  aria-label="Visa Application Name Home"
                  href="./horizontal-navigation"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Utility
                      vContainerHide="xs"
                      element={<Typography variant="headline-3">Application Name</Typography>}
                    />
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <UtilityFragment vFlex vJustifyContent="end" vFlexGrow vMarginLeft="auto" vContainerHide="mobile">
                <nav aria-label="Label for alternate horizontal example with active element">
                  <UtilityFragment vGap={4}>
                    <Tabs>
                      <Tab>
                        <Button
                          aria-current="page"
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 1</a>}
                        />
                      </Tab>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 2</a>}
                        />
                      </Tab>
                      <Tab>
                        <DropdownButton
                          aria-expanded={label3Open}
                          aria-controls={label3Open ? `${id}-label-dropdown-menu` : undefined}
                          id={`${id}-label-dropdown-button`}
                          buttonSize="large"
                          colorScheme="tertiary"
                          ref={label3FloatingRefs.setReference}
                          {...getLabel3ReferenceProps()}
                        >
                          L1 label 3<TabSuffix element={label3Open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                        </DropdownButton>

                        {label3Open && (
                          <FloatingFocusManager
                            context={label3FloatingContext}
                            modal={false}
                            initialFocus={-1}
                            restoreFocus={true}
                          >
                            <DropdownMenu
                              id={`${id}-label-dropdown-menu`}
                              aria-hidden={!label3Open}
                              style={
                                {
                                  inlineSize: '180px',
                                  position: 'absolute',
                                  ...label3FloatingStyles,
                                  zIndex: 1,
                                } as CSSProperties
                              }
                              ref={label3FloatingRefs.setFloating}
                              {...getLabel3FloatingProps()}
                            >
                              <Listbox>
                                {label3SubItems.map(label3SubItem => (
                                  <li key={label3SubItem.id}>
                                    <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                      <ListboxItem href={label3SubItem.href} tag="a">
                                        {label3SubItem.tabLabel}
                                      </ListboxItem>
                                    </UtilityFragment>
                                  </li>
                                ))}
                              </Listbox>
                            </DropdownMenu>
                          </FloatingFocusManager>
                        )}
                      </Tab>
                    </Tabs>
                  </UtilityFragment>
                </nav>
              </UtilityFragment>
              <Utility vFlex vGap={8} vMarginLeft={8}>
                <Button
                  aria-label="search site"
                  buttonSize="large"
                  ref={searchButtonRef}
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => { setExpandSearch(true); searchInitiallyActivated.current = true; }}
                >
                  <VisaSearchLow />
                </Button>
                <UtilityFragment vContainerHide="mobile">
                  <Button
                    aria-label="notifications"
                    aria-describedby={`${id}-notifications-badge`}
                    buttonSize="large"
                    colorScheme="tertiary"
                    iconButton
                  >
                    <VisaNotificationsLow />
                    <Badge id={`${id}-notifications-badge`} badgeVariant="number" tag="sup">
                      3
                    </Badge>
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile">
                  <Tab tag="div">
                    <DropdownButton
                      aria-expanded={accountMenuOpen}
                      aria-controls={accountMenuOpen ? `${id}-account-menu` : undefined}
                      aria-label="Alex Miller"
                      buttonSize="large"
                      colorScheme="tertiary"
                      element={<Avatar tag="button" />}
                      ref={accountFloatingRefs.setReference}
                      {...getAccountReferenceProps()}
                    >
                      <VisaAccountLow />
                      <TabSuffix element={accountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </DropdownButton>
                    {accountMenuOpen && (
                      <FloatingFocusManager
                        context={accountFloatingContext}
                        modal={false}
                        initialFocus={-1}
                        restoreFocus={true}
                      >
                        <DropdownMenu
                          id={`${id}-account-menu`}
                          aria-hidden={!accountMenuOpen}
                          style={
                            {
                              inlineSize: '180px',
                              position: 'absolute',
                              ...accountFloatingStyles,
                              zIndex: 1,
                            } as CSSProperties
                          }
                          ref={accountFloatingRefs.setFloating}
                          {...getAccountFloatingProps()}
                        >
                          <Listbox>
                            {accountSubItems.map(accountSubItem => (
                              <UtilityFragment key={accountSubItem.id}>
                                <li>
                                  <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                    <ListboxItem href={accountSubItem.href} tag="a">
                                      {accountSubItem.tabLabel}
                                    </ListboxItem>
                                  </UtilityFragment>
                                </li>
                              </UtilityFragment>
                            ))}
                          </Listbox>
                        </DropdownMenu>
                      </FloatingFocusManager>
                    )}
                  </Tab>
                </UtilityFragment>
              </Utility>
            </>
          ) : (
            <UtilityFragment vFlex>
              <Surface
                style={
                  {
                    '--v-surface-background': 'var(--palette-default-surface-3)',
                    '--v-surface-border-radius': 'var(--size-rounded-medium)',
                    '--v-surface-padding-inline': 'var(--size-scalable-8)',
                  } as CSSProperties
                }
              >
                <InputContainer>
                  <VisaSearchLow />
                  <Input
                    id={`${id}-search-field`}
                    name={`${id}-search-field`}
                    ref={searchInputRef}
                    required
                    type="search"
                    aria-label="Search"
                    placeholder="Search"
                  />
                </InputContainer>
                <Button
                  aria-label="close search"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => setExpandSearch(false)}
                >
                  <VisaCloseLow />
                </Button>
              </Surface>
            </UtilityFragment>
          )}
        </Nav>
      </UtilityFragment>
      <UtilityFragment vContainerHide="desktop" vHide={!mobileMenuOpen}>
        <Nav
          alternate
          aria-label="Label for alternate horizontal example with active element"
          aria-hidden={!mobileMenuOpen}
          id={`${id}-mobile-menu`}
          orientation="vertical"
        >
          <Tabs orientation="vertical">
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 1</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 2</a>}
              />
            </Tab>
            <Tab>
              <Button
                aria-expanded={mobileLabel3MenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                id={`${id}-mobile-menu-label-dropdown-button`}
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileLabel3MenuOpen(!mobileLabel3MenuOpen)}
              >
                L1 Label 3
                <TabSuffix element={mobileLabel3MenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileLabel3MenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {label3SubItems.map(label3SubItem => (
                    <Tab key={label3SubItem.id} id={label3SubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={label3SubItem.href}>{label3SubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 3</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                style={{ wordBreak: 'break-word', blockSize: 'max-content' } as CSSProperties}
              >
                Notifications
                <Badge badgeVariant="number" style={{ position: 'relative' }} tag="sup">
                  3
                </Badge>
              </Button>
            </Tab>
            <Divider dividerType="decorative"></Divider>
            <Tab tag="div">
              <Button
                aria-expanded={mobileAccountMenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                aria-label="Alex Miller"
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileAccountMenuOpen(!mobileAccountMenuOpen)}
              >
                <VisaAccountLow />
                Alex Miller
                <TabSuffix element={mobileAccountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileAccountMenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {accountSubItems.map(accountSubItem => (
                    <Tab key={accountSubItem.id} id={accountSubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
          </Tabs>
        </Nav>
      </UtilityFragment>
    </div>
  );
};

```

### Alternate horizontal navigation with icons
- **Section**: Default horizontal navigations
- **URL**: components/horizontal-navigation/alternate-horizontal-with-icons
- **Tags**: docs
```tsx
import {
  autoUpdate,
  FloatingFocusManager,
  offset,
  useClick,
  useFloating,
  useInteractions,
  useDismiss,
} from '@floating-ui/react';

import {
  VisaAccountLow,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseLow,
  VisaCloseTiny,
  VisaMenuLow,
  VisaNotificationsLow,
  VisaSearchLow,
  VisaSecurityTiny,
  VisaSettingsTiny,
  VisaStatisticsTiny,
} from '@visa/nova-icons-react';
import {
  Avatar,
  Badge,
  Button,
  Divider,
  DropdownButton,
  DropdownMenu,
  Input,
  InputContainer,
  Link,
  Listbox,
  ListboxItem,
  Nav,
  NavAppName,
  Surface,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useEffect, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'alternate-horizontal-nav-with-icons';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './horizontal-navigation',
  },
];

const label3SubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-label-3-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-label-3-sub-item-1`,
    href: './horizontal-navigation',
  },
];

export const AlternateHorizontalNavWithIcons = () => {
  const searchInputRef = useRef<HTMLInputElement | null>();
  const searchButtonRef = useRef<HTMLButtonElement | null>();

  const [accountMenuOpen, setAccountMenuOpen] = useState(false);
  const [mobileAccountMenuOpen, setMobileAccountMenuOpen] = useState(false);
  const [mobileLabel3MenuOpen, setMobileLabel3MenuOpen] = useState(false);
  const [expandSearch, setExpandSearch] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [label3Open, setLabel3Open] = useState(false);
  const searchInitiallyActivated = useRef(false);

  useEffect(() => {
    if (expandSearch && searchInitiallyActivated.current) {
      searchInputRef.current?.focus();
    }
    if (!expandSearch && searchInitiallyActivated.current) {
      searchButtonRef.current?.focus();
    }
  }, [expandSearch]);

  // For dropdown menus in the horizontal nav, we use floating UI for
  // -opening
  // -positioning
  // -dismissing

  // floating-ui setup for the account dropdown
  const {
    context: accountFloatingContext,
    floatingStyles: accountFloatingStyles,
    refs: accountFloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-end',
    whileElementsMounted: autoUpdate,
  });
  const clickAccountRef = useClick(accountFloatingContext);
  const dismissAccountMenu = useDismiss(accountFloatingContext);
  const { getReferenceProps: getAccountReferenceProps, getFloatingProps: getAccountFloatingProps } = useInteractions([
    clickAccountRef,
    dismissAccountMenu,
  ]);

  // floating-ui setup for the label3 tab dropdown
  const {
    context: label3FloatingContext,
    floatingStyles: label3FloatingStyles,
    refs: label3FloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: label3Open,
    onOpenChange: setLabel3Open,
    placement: 'bottom-start',
    whileElementsMounted: autoUpdate,
  });
  const clickLabel3Ref = useClick(label3FloatingContext);
  const dismissLabel3Menu = useDismiss(label3FloatingContext);
  const { getReferenceProps: getLabel3ReferenceProps, getFloatingProps: getLabel3FloatingProps } = useInteractions([
    clickLabel3Ref,
    dismissLabel3Menu,
  ]);

  const onToggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div>
      <Link alternate skipLink href="#content">
        Skip to content
      </Link>
      <UtilityFragment vJustifyContent="between">
        <Nav id={id} alternate orientation="horizontal" tag="header">
          {!expandSearch ? (
            <>
              <UtilityFragment vContainerHide="desktop">
                <DropdownButton
                  aria-controls={`${id}-mobile-menu`}
                  aria-expanded={mobileMenuOpen ? 'true' : 'false'}
                  aria-describedby={`${id}-mobile-menu-notifications-badge`}
                  aria-label="open menu"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  id={`${id}-mobile-menu-button`}
                  onClick={onToggleMobileMenu}
                >
                  {mobileMenuOpen ? (
                    <VisaCloseTiny />
                  ) : (
                    <>
                      <VisaMenuLow />
                      <Badge
                        id={`${id}-mobile-menu-notifications-badge`}
                        aria-label="3 notifications"
                        badgeVariant="number"
                        tag="sup"
                      >
                        3
                      </Badge>
                    </>
                  )}
                </DropdownButton>
              </UtilityFragment>
              <UtilityFragment vFlex vGap={16}>
                <Link
                  aria-label="Visa Application Name Home"
                  href="./horizontal-navigation"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Utility
                      vContainerHide="xs"
                      element={<Typography variant="headline-3">Application Name</Typography>}
                    />
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <UtilityFragment vFlex vJustifyContent="end" vFlexGrow vMarginLeft="auto" vContainerHide="mobile">
                <nav aria-label="Label for alternate horizontal example with icons">
                  <UtilityFragment vGap={4}>
                    <Tabs>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">{<VisaStatisticsTiny />}L1 label 1</a>}
                        />
                      </Tab>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">{<VisaSettingsTiny />}L1 label 2</a>}
                        />
                      </Tab>
                      <Tab>
                        <DropdownButton
                          aria-expanded={label3Open}
                          aria-controls={label3Open ? `${id}-label-dropdown-menu` : undefined}
                          id={`${id}-label-dropdown-button`}
                          buttonSize="large"
                          colorScheme="tertiary"
                          ref={label3FloatingRefs.setReference}
                          {...getLabel3ReferenceProps()}
                        >
                          <VisaSecurityTiny />
                          L1 label 3<TabSuffix element={label3Open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                        </DropdownButton>

                        {label3Open && (
                          <FloatingFocusManager
                            context={label3FloatingContext}
                            modal={false}
                            initialFocus={-1}
                            restoreFocus={true}
                          >
                            <DropdownMenu
                              id={`${id}-label-dropdown-menu`}
                              aria-hidden={!label3Open}
                              style={
                                {
                                  inlineSize: '180px',
                                  position: 'absolute',
                                  ...label3FloatingStyles,
                                  zIndex: 1,
                                } as CSSProperties
                              }
                              ref={label3FloatingRefs.setFloating}
                              {...getLabel3FloatingProps()}
                            >
                              <Listbox>
                                {label3SubItems.map(label3SubItem => (
                                  <li key={label3SubItem.id}>
                                    <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                      <ListboxItem href={label3SubItem.href} tag="a">
                                        {label3SubItem.tabLabel}
                                      </ListboxItem>
                                    </UtilityFragment>
                                  </li>
                                ))}
                              </Listbox>
                            </DropdownMenu>
                          </FloatingFocusManager>
                        )}
                      </Tab>
                    </Tabs>
                  </UtilityFragment>
                </nav>
              </UtilityFragment>
              <Utility vFlex vGap={8} vMarginLeft={8}>
                <Button
                  aria-label="search site"
                  buttonSize="large"
                  ref={searchButtonRef}
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => { setExpandSearch(true); searchInitiallyActivated.current = true; }}
                >
                  <VisaSearchLow />
                </Button>
                <UtilityFragment vContainerHide="mobile">
                  <Button
                    aria-label="notifications"
                    aria-describedby={`${id}-notifications-badge`}
                    buttonSize="large"
                    colorScheme="tertiary"
                    iconButton
                  >
                    <VisaNotificationsLow />
                    <Badge id={`${id}-notifications-badge`} badgeVariant="number" tag="sup">
                      3
                    </Badge>
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile">
                  <Tab tag="div">
                    <DropdownButton
                      aria-expanded={accountMenuOpen}
                      aria-controls={accountMenuOpen ? `${id}-account-menu` : undefined}
                      aria-label="Alex Miller"
                      buttonSize="large"
                      colorScheme="tertiary"
                      element={<Avatar tag="button" />}
                      ref={accountFloatingRefs.setReference}
                      {...getAccountReferenceProps()}
                    >
                      <VisaAccountLow />
                      <TabSuffix element={accountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </DropdownButton>
                    {accountMenuOpen && (
                      <FloatingFocusManager
                        context={accountFloatingContext}
                        modal={false}
                        initialFocus={-1}
                        restoreFocus={true}
                      >
                        <DropdownMenu
                          id={`${id}-account-menu`}
                          aria-hidden={!accountMenuOpen}
                          style={
                            {
                              inlineSize: '180px',
                              position: 'absolute',
                              ...accountFloatingStyles,
                              zIndex: 1,
                            } as CSSProperties
                          }
                          ref={accountFloatingRefs.setFloating}
                          {...getAccountFloatingProps()}
                        >
                          <Listbox>
                            {accountSubItems.map(accountSubItem => (
                              <UtilityFragment key={accountSubItem.id}>
                                <li>
                                  <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                    <ListboxItem href={accountSubItem.href} tag="a">
                                      {accountSubItem.tabLabel}
                                    </ListboxItem>
                                  </UtilityFragment>
                                </li>
                              </UtilityFragment>
                            ))}
                          </Listbox>
                        </DropdownMenu>
                      </FloatingFocusManager>
                    )}
                  </Tab>
                </UtilityFragment>
              </Utility>
            </>
          ) : (
            <UtilityFragment vFlex>
              <Surface
                style={
                  {
                    '--v-surface-background': 'var(--palette-default-surface-3)',
                    '--v-surface-border-radius': 'var(--size-rounded-medium)',
                    '--v-surface-padding-inline': 'var(--size-scalable-8)',
                  } as CSSProperties
                }
              >
                <InputContainer>
                  <VisaSearchLow />
                  <Input
                    id={`${id}-search-field`}
                    name={`${id}-search-field`}
                    ref={searchInputRef}
                    required
                    type="search"
                    aria-label="Search"
                    placeholder="Search"
                  />
                </InputContainer>
                <Button
                  aria-label="close search"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => setExpandSearch(false)}
                >
                  <VisaCloseLow />
                </Button>
              </Surface>
            </UtilityFragment>
          )}
        </Nav>
      </UtilityFragment>
      <UtilityFragment vContainerHide="desktop" vHide={!mobileMenuOpen}>
        <Nav
          alternate
          aria-label="Label for alternate horizontal example with icons"
          aria-hidden={!mobileMenuOpen}
          id={`${id}-mobile-menu`}
          orientation="vertical"
        >
          <Tabs orientation="vertical">
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 1</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 2</a>}
              />
            </Tab>
            <Tab>
              <Button
                aria-expanded={mobileLabel3MenuOpen}
                aria-controls={mobileLabel3MenuOpen ? `${id}-account-sub-menu` : 'undefined'}
                id={`${id}-mobile-menu-label-dropdown-button`}
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileLabel3MenuOpen(!mobileLabel3MenuOpen)}
              >
                L1 Label 3
                <TabSuffix element={mobileLabel3MenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>

              {mobileLabel3MenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {label3SubItems.map(label3SubItem => (
                    <Tab key={label3SubItem.id} id={label3SubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={label3SubItem.href}>{label3SubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                style={{ wordBreak: 'break-word', blockSize: 'max-content' } as CSSProperties}
              >
                Notifications
                <Badge
                  badgeVariant="number"
                  tag="sup"
                  style={
                    {
                      position: 'relative',
                    } as CSSProperties
                  }
                >
                  3
                </Badge>
              </Button>
            </Tab>
            <Divider dividerType="decorative"></Divider>
            <Tab tag="div">
              <Button
                aria-expanded={mobileAccountMenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                aria-label="Alex Miller"
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileAccountMenuOpen(!mobileAccountMenuOpen)}
              >
                <VisaAccountLow />
                Alex Miller
                <TabSuffix element={mobileAccountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileAccountMenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {accountSubItems.map(accountSubItem => (
                    <Tab key={accountSubItem.id} id={accountSubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
          </Tabs>
        </Nav>
      </UtilityFragment>
    </div>
  );
};

```

### Stacked horizontal navigation
- **Section**: Default horizontal navigations
- **URL**: components/horizontal-navigation/stacked-horizontal-nav
- **Tags**: docs
```tsx
import {
  autoUpdate,
  FloatingFocusManager,
  offset,
  useClick,
  useFloating,
  useInteractions,
  useDismiss,
} from '@floating-ui/react';
import {
  VisaAccountLow,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseLow,
  VisaCloseTiny,
  VisaMenuLow,
  VisaNotificationsLow,
  VisaSearchLow,
} from '@visa/nova-icons-react';
import {
  Avatar,
  Badge,
  Button,
  Divider,
  DropdownButton,
  DropdownMenu,
  Input,
  InputContainer,
  Link,
  Listbox,
  ListboxItem,
  Nav,
  NavAppName,
  Surface,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useEffect, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'stacked-horizontal-nav';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './horizontal-navigation',
  },
];

export const StackedHorizontalNav = () => {
  const searchInputRef = useRef<HTMLInputElement | null>();
  const searchButtonRef = useRef<HTMLButtonElement | null>();

  const [accountMenuOpen, setAccountMenuOpen] = useState(false);
  const [mobileAccountMenuOpen, setMobileAccountMenuOpen] = useState(false);
  const [expandSearch, setExpandSearch] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const searchInitiallyActivated = useRef(false);

  useEffect(() => {
    if (expandSearch && searchInitiallyActivated.current) {
      searchInputRef.current?.focus();
    }
    if (!expandSearch && searchInitiallyActivated.current) {
      searchButtonRef.current?.focus();
    }
  }, [expandSearch]);

  // For dropdown menus in the horizontal nav, we use floating UI for
  // -opening
  // -positioning
  // -dismissing

  // floating-ui setup for the account dropdown
  const {
    context: accountFloatingContext,
    floatingStyles: accountFloatingStyles,
    refs: accountFloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-end',
    whileElementsMounted: autoUpdate,
  });
  const clickAccountRef = useClick(accountFloatingContext);
  const dismissAccountMenu = useDismiss(accountFloatingContext);
  const { getReferenceProps: getAccountReferenceProps, getFloatingProps: getAccountFloatingProps } = useInteractions([
    clickAccountRef,
    dismissAccountMenu,
  ]);

  const onToggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div>
      <Link skipLink href="#content">
        Skip to content
      </Link>
      <UtilityFragment vJustifyContent="between">
        <Nav id={id} orientation="horizontal" tag="header">
          {!expandSearch ? (
            <>
              <UtilityFragment vContainerHide="desktop">
                <DropdownButton
                  aria-controls={`${id}-mobile-menu`}
                  aria-expanded={mobileMenuOpen ? 'true' : 'false'}
                  aria-describedby={`${id}-mobile-menu-notifications-badge`}
                  aria-label="open menu"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  id={`${id}-mobile-menu-button`}
                  onClick={onToggleMobileMenu}
                >
                  {mobileMenuOpen ? (
                    <VisaCloseTiny />
                  ) : (
                    <>
                      <VisaMenuLow />
                      <Badge
                        id={`${id}-mobile-menu-notifications-badge`}
                        aria-label="3 notifications"
                        badgeVariant="number"
                      >
                        3
                      </Badge>
                    </>
                  )}
                </DropdownButton>
              </UtilityFragment>
              <UtilityFragment vFlex vGap={16}>
                <Link
                  aria-label="Visa Application Name Home"
                  href="./horizontal-navigation"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Utility
                      vContainerHide="xs"
                      element={<Typography variant="headline-3">Application Name</Typography>}
                    />
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <Utility vFlex vGap={8} vMarginLeft={8}>
                <Button
                  aria-label="search site"
                  buttonSize="large"
                  ref={searchButtonRef}
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => { setExpandSearch(true); searchInitiallyActivated.current = true; }}
                >
                  <VisaSearchLow />
                </Button>
                <UtilityFragment vContainerHide="mobile">
                  <Button
                    aria-label="notifications"
                    aria-describedby={`${id}-notifications-badge`}
                    buttonSize="large"
                    colorScheme="tertiary"
                    iconButton
                  >
                    <VisaNotificationsLow />
                    <Badge id={`${id}-notifications-badge`} badgeVariant="number">
                      3
                    </Badge>
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile">
                  <Tab tag="div">
                    <DropdownButton
                      aria-expanded={accountMenuOpen}
                      aria-controls={accountMenuOpen ? `${id}-account-menu` : undefined}
                      aria-label="Alex Miller"
                      buttonSize="large"
                      colorScheme="tertiary"
                      element={<Avatar tag="button" />}
                      ref={accountFloatingRefs.setReference}
                      {...getAccountReferenceProps()}
                    >
                      <VisaAccountLow />
                      <TabSuffix element={accountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </DropdownButton>
                    {accountMenuOpen && (
                      <FloatingFocusManager
                        context={accountFloatingContext}
                        modal={false}
                        initialFocus={-1}
                        restoreFocus={true}
                      >
                        <DropdownMenu
                          id={`${id}-account-menu`}
                          aria-hidden={!accountMenuOpen}
                          style={
                            {
                              inlineSize: '180px',
                              position: 'absolute',
                              ...accountFloatingStyles,
                              zIndex: 1,
                            } as CSSProperties
                          }
                          ref={accountFloatingRefs.setFloating}
                          {...getAccountFloatingProps()}
                        >
                          <Listbox>
                            {accountSubItems.map(accountSubItem => (
                              <UtilityFragment key={accountSubItem.id}>
                                <li>
                                  <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                    <ListboxItem href={accountSubItem.href} tag="a">
                                      {accountSubItem.tabLabel}
                                    </ListboxItem>
                                  </UtilityFragment>
                                </li>
                              </UtilityFragment>
                            ))}
                          </Listbox>
                        </DropdownMenu>
                      </FloatingFocusManager>
                    )}
                  </Tab>
                </UtilityFragment>
              </Utility>
            </>
          ) : (
            <UtilityFragment vFlex>
              <Surface
                style={
                  {
                    '--v-surface-background': 'var(--palette-default-surface-3)',
                    '--v-surface-border-radius': 'var(--size-rounded-medium)',
                    '--v-surface-padding-inline': 'var(--size-scalable-8)',
                  } as CSSProperties
                }
              >
                <InputContainer>
                  <VisaSearchLow />
                  <Input
                    id={`${id}-search-field`}
                    name={`${id}-search-field`}
                    ref={searchInputRef}
                    required
                    type="search"
                    aria-label="Search"
                    placeholder="Search"
                  />
                </InputContainer>
                <Button
                  aria-label="close search"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => setExpandSearch(false)}
                >
                  <VisaCloseLow />
                </Button>
              </Surface>
            </UtilityFragment>
          )}
        </Nav>
      </UtilityFragment>
      <Nav
        aria-label="Label for horizontal example with stacked menu"
        className="v-ml-auto v-mobile-container-hide"
        style={
          {
            '--v-surface-background': 'var(--palette-default-surface-2)',
            '--v-tabs-active-line-padding': 'var(--size-responsive-10)',
          } as CSSProperties
        }
      >
        <Tabs className="v-gap-8">
          <Tab>
            <Button
              buttonSize="large"
              colorScheme="tertiary"
              element={<a href="./horizontal-navigation">L1 label 1</a>}
            />
          </Tab>
          <Tab>
            <Button
              buttonSize="large"
              colorScheme="tertiary"
              element={<a href="./horizontal-navigation">L1 label 2</a>}
            />
          </Tab>
          <Tab>
            <Button
              buttonSize="large"
              colorScheme="tertiary"
              element={<a href="./horizontal-navigation">L1 label 3</a>}
            />
          </Tab>
        </Tabs>
      </Nav>
      <UtilityFragment vContainerHide="desktop" vHide={!mobileMenuOpen}>
        <Nav
          aria-label="Label for horizontal example with stacked menu"
          aria-hidden={!mobileMenuOpen}
          id={`${id}-mobile-menu`}
          orientation="vertical"
        >
          <Tabs orientation="vertical">
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 1</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 2</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 3</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                style={{ wordBreak: 'break-word', blockSize: 'max-content' } as CSSProperties}
              >
                Notifications
                <Badge badgeVariant="number" style={{ position: 'relative' }}>
                  3
                </Badge>
              </Button>
            </Tab>
            <Divider dividerType="decorative"></Divider>
            <Tab tag="div">
              <Button
                aria-expanded={mobileAccountMenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                aria-label="Alex Miller"
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileAccountMenuOpen(!mobileAccountMenuOpen)}
              >
                <VisaAccountLow />
                Alex Miller
                <TabSuffix element={mobileAccountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileAccountMenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {accountSubItems.map(accountSubItem => (
                    <Tab key={accountSubItem.id} id={accountSubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
          </Tabs>
        </Nav>
      </UtilityFragment>
    </div>
  );
};

```

### Default horizontal navigation with persistent search
- **Section**: Horizontal navigations with persistent search
- **URL**: components/horizontal-navigation/search-persistent-horizontal-nav
- **Tags**: docs
```tsx
import {
  autoUpdate,
  FloatingFocusManager,
  offset,
  useClick,
  useFloating,
  useInteractions,
  useDismiss,
} from '@floating-ui/react';
import {
  VisaAccountLow,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseTiny,
  VisaCloseLow,
  VisaMenuLow,
  VisaNotificationsLow,
  VisaSearchLow,
} from '@visa/nova-icons-react';
import {
  Avatar,
  Badge,
  Button,
  Divider,
  DropdownButton,
  DropdownMenu,
  Input,
  InputContainer,
  Link,
  Listbox,
  ListboxItem,
  Nav,
  NavAppName,
  Surface,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useEffect, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'search-persistent-horizontal-nav';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './horizontal-navigation',
  },
];

const label3SubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-label-3-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-label-3-sub-item-1`,
    href: './horizontal-navigation',
  },
];

export const SearchPersistentHorizontalNav = () => {
  const [accountMenuOpen, setAccountMenuOpen] = useState(false);
  const [mobileAccountMenuOpen, setMobileAccountMenuOpen] = useState(false);
  const [mobileLabel3MenuOpen, setMobileLabel3MenuOpen] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [label3Open, setLabel3Open] = useState(false);

  const mobileSearchInputRef = useRef<HTMLInputElement | null>();
  const mobileSearchButtonRef = useRef<HTMLButtonElement | null>();

  const [expandSearch, setExpandSearch] = useState(false);

  useEffect(() => {
    if (expandSearch) {
      mobileSearchInputRef.current?.focus();
    }
    if (!expandSearch) {
      mobileSearchButtonRef.current?.focus();
    }
  }, [expandSearch]);

  // For dropdown menus in the horizontal nav, we use floating UI for
  // -opening
  // -positioning
  // -dismissing

  // floating-ui setup for the account dropdown
  const {
    context: accountFloatingContext,
    floatingStyles: accountFloatingStyles,
    refs: accountFloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-end',
    whileElementsMounted: autoUpdate,
  });
  const clickAccountRef = useClick(accountFloatingContext);
  const dismissAccountMenu = useDismiss(accountFloatingContext);
  const { getReferenceProps: getAccountReferenceProps, getFloatingProps: getAccountFloatingProps } = useInteractions([
    clickAccountRef,
    dismissAccountMenu,
  ]);

  // floating-ui setup for the label3 tab dropdown
  const {
    context: label3FloatingContext,
    floatingStyles: label3FloatingStyles,
    refs: label3FloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: label3Open,
    onOpenChange: setLabel3Open,
    placement: 'bottom-start',
    whileElementsMounted: autoUpdate,
  });
  const clickLabel3Ref = useClick(label3FloatingContext);
  const dismissLabel3Menu = useDismiss(label3FloatingContext);
  const { getReferenceProps: getLabel3ReferenceProps, getFloatingProps: getLabel3FloatingProps } = useInteractions([
    clickLabel3Ref,
    dismissLabel3Menu,
  ]);

  const onToggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div>
      <Link skipLink href="#content">
        Skip to content
      </Link>
      <UtilityFragment vJustifyContent="between">
        <Nav id={id} orientation="horizontal" tag="header">
          {!expandSearch ? (
            <>
              <UtilityFragment vContainerHide="desktop">
                <DropdownButton
                  aria-controls={`${id}-mobile-menu`}
                  aria-expanded={mobileMenuOpen ? 'true' : 'false'}
                  aria-describedby={`${id}-mobile-menu-notifications-badge`}
                  aria-label="open menu"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  id={`${id}-mobile-menu-button`}
                  onClick={onToggleMobileMenu}
                >
                  {mobileMenuOpen ? (
                    <VisaCloseTiny />
                  ) : (
                    <>
                      <VisaMenuLow />
                      <Badge
                        id={`${id}-mobile-menu-notifications-badge`}
                        aria-label="3 notifications"
                        badgeVariant="number"
                        tag="sup"
                      >
                        3
                      </Badge>
                    </>
                  )}
                </DropdownButton>
              </UtilityFragment>
              <UtilityFragment vFlex vGap={16}>
                <Link
                  aria-label="Visa Application Name Home"
                  href="./horizontal-navigation"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Utility
                      vContainerHide="xs"
                      element={<Typography variant="headline-3">Application Name</Typography>}
                    />
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <UtilityFragment vFlex vJustifyContent="end" vFlexGrow vMarginLeft="auto" vContainerHide="mobile">
                <nav aria-label="Label for horizontal example with persistent search">
                  <UtilityFragment vGap={4}>
                    <Tabs>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 1</a>}
                        />
                      </Tab>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 2</a>}
                        />
                      </Tab>
                      <Tab>
                        <DropdownButton
                          aria-expanded={label3Open}
                          aria-controls={label3Open ? `${id}-label-dropdown-menu` : undefined}
                          id={`${id}-label-dropdown-button`}
                          buttonSize="large"
                          colorScheme="tertiary"
                          ref={label3FloatingRefs.setReference}
                          {...getLabel3ReferenceProps()}
                        >
                          L1 label 3<TabSuffix element={label3Open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                        </DropdownButton>

                        {label3Open && (
                          <FloatingFocusManager
                            context={label3FloatingContext}
                            modal={false}
                            initialFocus={-1}
                            restoreFocus={true}
                          >
                            <DropdownMenu
                              id={`${id}-label-dropdown-menu`}
                              aria-hidden={!label3Open}
                              style={
                                {
                                  inlineSize: '180px',
                                  position: 'absolute',
                                  ...label3FloatingStyles,
                                  zIndex: 1,
                                } as CSSProperties
                              }
                              ref={label3FloatingRefs.setFloating}
                              {...getLabel3FloatingProps()}
                            >
                              <Listbox>
                                {label3SubItems.map(label3SubItem => (
                                  <li key={label3SubItem.id}>
                                    <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                      <ListboxItem href={label3SubItem.href} tag="a">
                                        {label3SubItem.tabLabel}
                                      </ListboxItem>
                                    </UtilityFragment>
                                  </li>
                                ))}
                              </Listbox>
                            </DropdownMenu>
                          </FloatingFocusManager>
                        )}
                      </Tab>
                    </Tabs>
                  </UtilityFragment>
                </nav>
              </UtilityFragment>
              <Utility vFlex vGap={8} vMarginLeft={8}>
                <UtilityFragment vFlexRow vContainerHide="mobile">
                  <InputContainer>
                    <VisaSearchLow />
                    <Input
                      id={`${id}-search-field`}
                      name={`${id}-search-field`}
                      required
                      type="search"
                      aria-label="Search"
                      placeholder="Search"
                    />
                  </InputContainer>
                </UtilityFragment>
                <UtilityFragment vFlexRow vContainerHide="desktop">
                  <Button
                    aria-label="search site"
                    buttonSize="large"
                    ref={mobileSearchButtonRef}
                    colorScheme="tertiary"
                    iconButton
                    onClick={() => {
                      setExpandSearch(true);
                    }}
                  >
                    <VisaSearchLow />
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile">
                  <Button
                    aria-label="notifications"
                    aria-describedby={`${id}-notifications-badge`}
                    buttonSize="large"
                    colorScheme="tertiary"
                    iconButton
                  >
                    <VisaNotificationsLow />
                    <Badge id={`${id}-notifications-badge`} badgeVariant="number" tag="sup">
                      3
                    </Badge>
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile" vPaddingBottom={0}>
                  <Tab tag="div">
                    <DropdownButton
                      aria-expanded={accountMenuOpen}
                      aria-controls={accountMenuOpen ? `${id}-account-menu` : undefined}
                      aria-label="Alex Miller"
                      buttonSize="large"
                      colorScheme="tertiary"
                      element={<Avatar tag="button" />}
                      ref={accountFloatingRefs.setReference}
                      {...getAccountReferenceProps()}
                    >
                      <VisaAccountLow />
                      <TabSuffix element={accountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </DropdownButton>
                    {accountMenuOpen && (
                      <FloatingFocusManager
                        context={accountFloatingContext}
                        modal={false}
                        initialFocus={-1}
                        restoreFocus={true}
                      >
                        <DropdownMenu
                          id={`${id}-account-menu`}
                          aria-hidden={!accountMenuOpen}
                          style={
                            {
                              inlineSize: '180px',
                              position: 'absolute',
                              ...accountFloatingStyles,
                              zIndex: 1,
                            } as CSSProperties
                          }
                          ref={accountFloatingRefs.setFloating}
                          {...getAccountFloatingProps()}
                        >
                          <Listbox>
                            {accountSubItems.map(accountSubItem => (
                              <UtilityFragment key={accountSubItem.id}>
                                <li>
                                  <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                    <ListboxItem href={accountSubItem.href} tag="a">
                                      {accountSubItem.tabLabel}
                                    </ListboxItem>
                                  </UtilityFragment>
                                </li>
                              </UtilityFragment>
                            ))}
                          </Listbox>
                        </DropdownMenu>
                      </FloatingFocusManager>
                    )}
                  </Tab>
                </UtilityFragment>
              </Utility>
            </>
          ) : (
            <UtilityFragment vFlex>
              <Surface
                style={
                  {
                    '--v-surface-background': 'var(--palette-default-surface-3)',
                    '--v-surface-border-radius': 'var(--size-rounded-medium)',
                    '--v-surface-padding-inline': 'var(--size-scalable-8)',
                  } as CSSProperties
                }
              >
                <InputContainer>
                  <VisaSearchLow />
                  <Input
                    id={`${id}-search-field`}
                    name={`${id}-search-field`}
                    ref={mobileSearchInputRef}
                    required
                    type="search"
                    aria-label="Search"
                    placeholder="Search"
                  />
                </InputContainer>
                <Button
                  aria-label="close search"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => setExpandSearch(false)}
                >
                  <VisaCloseLow />
                </Button>
              </Surface>
            </UtilityFragment>
          )}
        </Nav>
      </UtilityFragment>
      <UtilityFragment vContainerHide="desktop" vHide={!mobileMenuOpen}>
        <Nav
          aria-label="Label for horizontal example with persistent search"
          aria-hidden={!mobileMenuOpen}
          id={`${id}-mobile-menu`}
          orientation="vertical"
        >
          <Tabs orientation="vertical">
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 1</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 2</a>}
              />
            </Tab>
            <Tab>
              <Button
                aria-expanded={mobileLabel3MenuOpen}
                aria-controls={mobileLabel3MenuOpen ? `${id}-account-sub-menu` : 'undefined'}
                id={`${id}-mobile-menu-label-dropdown-button`}
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileLabel3MenuOpen(!mobileLabel3MenuOpen)}
              >
                L1 Label 3
                <TabSuffix element={mobileLabel3MenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>

              {mobileLabel3MenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {label3SubItems.map(label3SubItem => (
                    <Tab key={label3SubItem.id} id={label3SubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={label3SubItem.href}>{label3SubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                style={{ wordBreak: 'break-word', blockSize: 'max-content' } as CSSProperties}
              >
                Notifications
                <Badge badgeVariant="number" style={{ position: 'relative' }} tag="sup">
                  3
                </Badge>
              </Button>
            </Tab>
            <Divider dividerType="decorative"></Divider>
            <Tab tag="div">
              <Button
                aria-expanded={mobileAccountMenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                aria-label="Alex Miller"
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileAccountMenuOpen(!mobileAccountMenuOpen)}
              >
                <VisaAccountLow />
                Alex Miller
                <TabSuffix element={mobileAccountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileAccountMenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {accountSubItems.map(accountSubItem => (
                    <Tab key={accountSubItem.id} id={accountSubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
          </Tabs>
        </Nav>
      </UtilityFragment>
    </div>
  );
};

```

### Stacked horizontal navigation with persistent search
- **Section**: Horizontal navigations with persistent search
- **URL**: components/horizontal-navigation/stacked-search-persistent-horizontal-nav
- **Tags**: docs
```tsx
import {
  autoUpdate,
  FloatingFocusManager,
  offset,
  useClick,
  useFloating,
  useInteractions,
  useDismiss,
} from '@floating-ui/react';
import {
  VisaAccountLow,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseTiny,
  VisaCloseLow,
  VisaMenuLow,
  VisaNotificationsLow,
  VisaSearchLow,
} from '@visa/nova-icons-react';
import {
  Avatar,
  Badge,
  Button,
  Divider,
  DropdownButton,
  DropdownMenu,
  Input,
  InputContainer,
  Link,
  Listbox,
  ListboxItem,
  Nav,
  NavAppName,
  Surface,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useEffect, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'stacked-search-persistent-horizontal-nav';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './horizontal-navigation',
  },
];

export const StackedSearchPersistentHorizontalNav = () => {
  const [accountMenuOpen, setAccountMenuOpen] = useState(false);
  const [mobileAccountMenuOpen, setMobileAccountMenuOpen] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const mobileSearchInputRef = useRef<HTMLInputElement | null>();
  const mobileSearchButtonRef = useRef<HTMLButtonElement | null>();

  const [expandSearch, setExpandSearch] = useState(false);

  useEffect(() => {
    if (expandSearch) {
      mobileSearchInputRef.current?.focus();
    }
    if (!expandSearch) {
      mobileSearchButtonRef.current?.focus();
    }
  }, [expandSearch]);

  // For dropdown menus in the horizontal nav, we use floating UI for
  // -opening
  // -positioning
  // -dismissing

  // floating-ui setup for the account dropdown
  const {
    context: accountFloatingContext,
    floatingStyles: accountFloatingStyles,
    refs: accountFloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-end',
    whileElementsMounted: autoUpdate,
  });
  const clickAccountRef = useClick(accountFloatingContext);
  const dismissAccountMenu = useDismiss(accountFloatingContext);
  const { getReferenceProps: getAccountReferenceProps, getFloatingProps: getAccountFloatingProps } = useInteractions([
    clickAccountRef,
    dismissAccountMenu,
  ]);

  const onToggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div>
      <Link skipLink href="#content">
        Skip to content
      </Link>
      <UtilityFragment vJustifyContent="between">
        <Nav id={id} orientation="horizontal" tag="header">
          {!expandSearch ? (
            <>
              <UtilityFragment vContainerHide="desktop">
                <DropdownButton
                  aria-controls={`${id}-mobile-menu`}
                  aria-expanded={mobileMenuOpen ? 'true' : 'false'}
                  aria-describedby={`${id}-mobile-menu-notifications-badge`}
                  aria-label="open menu"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  id={`${id}-mobile-menu-button`}
                  onClick={onToggleMobileMenu}
                >
                  {mobileMenuOpen ? (
                    <VisaCloseTiny />
                  ) : (
                    <>
                      <VisaMenuLow />
                      <Badge
                        id={`${id}-mobile-menu-notifications-badge`}
                        aria-label="3 notifications"
                        badgeVariant="number"
                      >
                        3
                      </Badge>
                    </>
                  )}
                </DropdownButton>
              </UtilityFragment>
              <UtilityFragment vFlex vGap={16}>
                <Link
                  aria-label="Visa Application Name Home"
                  href="./horizontal-navigation"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Utility
                      vContainerHide="xs"
                      element={<Typography variant="headline-3">Application Name</Typography>}
                    />
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <Utility vFlex vGap={8} vMarginLeft={8}>
                <UtilityFragment vFlexRow vContainerHide="xs">
                  <InputContainer>
                    <VisaSearchLow />
                    <Input
                      id={`${id}-search-field`}
                      name={`${id}-search-field`}
                      required
                      type="search"
                      aria-label="Search"
                      placeholder="Search"
                    />
                  </InputContainer>
                </UtilityFragment>
                <UtilityFragment vFlexRow vContainerHide="desktop">
                  <Button
                    aria-label="search site"
                    buttonSize="large"
                    ref={mobileSearchButtonRef}
                    colorScheme="tertiary"
                    iconButton
                    onClick={() => {
                      setExpandSearch(true);
                    }}
                  >
                    <VisaSearchLow />
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile">
                  <Button
                    aria-label="notifications"
                    aria-describedby={`${id}-notifications-badge`}
                    buttonSize="large"
                    colorScheme="tertiary"
                    iconButton
                  >
                    <VisaNotificationsLow />
                    <Badge id={`${id}-notifications-badge`} badgeVariant="number">
                      3
                    </Badge>
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile" vPaddingBottom={0}>
                  <Tab tag="div">
                    <DropdownButton
                      aria-expanded={accountMenuOpen}
                      aria-controls={accountMenuOpen ? `${id}-account-menu` : undefined}
                      aria-label="Alex Miller"
                      buttonSize="large"
                      colorScheme="tertiary"
                      element={<Avatar tag="button" />}
                      ref={accountFloatingRefs.setReference}
                      {...getAccountReferenceProps()}
                    >
                      <VisaAccountLow />
                      <TabSuffix element={accountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </DropdownButton>
                    {accountMenuOpen && (
                      <FloatingFocusManager
                        context={accountFloatingContext}
                        modal={false}
                        initialFocus={-1}
                        restoreFocus={true}
                      >
                        <DropdownMenu
                          id={`${id}-account-menu`}
                          aria-hidden={!accountMenuOpen}
                          style={
                            {
                              inlineSize: '180px',
                              position: 'absolute',
                              ...accountFloatingStyles,
                              zIndex: 1,
                            } as CSSProperties
                          }
                          ref={accountFloatingRefs.setFloating}
                          {...getAccountFloatingProps()}
                        >
                          <Listbox>
                            {accountSubItems.map(accountSubItem => (
                              <UtilityFragment key={accountSubItem.id}>
                                <li>
                                  <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                    <ListboxItem href={accountSubItem.href} tag="a">
                                      {accountSubItem.tabLabel}
                                    </ListboxItem>
                                  </UtilityFragment>
                                </li>
                              </UtilityFragment>
                            ))}
                          </Listbox>
                        </DropdownMenu>
                      </FloatingFocusManager>
                    )}
                  </Tab>
                </UtilityFragment>
              </Utility>
            </>
          ) : (
            <UtilityFragment vFlex>
              <Surface
                style={
                  {
                    '--v-surface-background': 'var(--palette-default-surface-3)',
                    '--v-surface-border-radius': 'var(--size-rounded-medium)',
                    '--v-surface-padding-inline': 'var(--size-scalable-8)',
                  } as CSSProperties
                }
              >
                <InputContainer>
                  <VisaSearchLow />
                  <Input
                    id={`${id}-search-field`}
                    name={`${id}-search-field`}
                    ref={mobileSearchInputRef}
                    required
                    type="search"
                    aria-label="Search"
                    placeholder="Search"
                  />
                </InputContainer>
                <Button
                  aria-label="close search"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => setExpandSearch(false)}
                >
                  <VisaCloseLow />
                </Button>
              </Surface>
            </UtilityFragment>
          )}
        </Nav>
      </UtilityFragment>

      <Nav
        aria-label="Label for horizontal example with stacked menu and persistent search"
        className="v-ml-auto v-mobile-container-hide"
        style={
          {
            '--v-surface-background': 'var(--palette-default-surface-2)',
            '--v-tabs-active-line-padding': 'var(--size-responsive-10)',
          } as CSSProperties
        }
      >
        <Tabs className="v-gap-8">
          <Tab>
            <Button
              buttonSize="large"
              colorScheme="tertiary"
              element={<a href="./horizontal-navigation">L1 label 1</a>}
            />
          </Tab>
          <Tab>
            <Button
              buttonSize="large"
              colorScheme="tertiary"
              element={<a href="./horizontal-navigation">L1 label 2</a>}
            />
          </Tab>
          <Tab>
            <Button
              buttonSize="large"
              colorScheme="tertiary"
              element={<a href="./horizontal-navigation">L1 label 3</a>}
            />
          </Tab>
        </Tabs>
      </Nav>
      <UtilityFragment vContainerHide="desktop" vHide={!mobileMenuOpen}>
        <Nav
          aria-label="Label for horizontal example with stacked menu and persistent search"
          aria-hidden={!mobileMenuOpen}
          id={`${id}-mobile-menu`}
          orientation="vertical"
        >
          <Tabs orientation="vertical">
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 1</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 2</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 3</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                style={{ wordBreak: 'break-word', blockSize: 'max-content' } as CSSProperties}
              >
                Notifications
                <Badge badgeVariant="number" style={{ position: 'relative' }}>
                  3
                </Badge>
              </Button>
            </Tab>
            <Divider dividerType="decorative"></Divider>
            <Tab tag="div">
              <Button
                aria-expanded={mobileAccountMenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                aria-label="Alex Miller"
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileAccountMenuOpen(!mobileAccountMenuOpen)}
              >
                <VisaAccountLow />
                Alex Miller
                <TabSuffix element={mobileAccountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileAccountMenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {accountSubItems.map(accountSubItem => (
                    <Tab key={accountSubItem.id} id={accountSubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
          </Tabs>
        </Nav>
      </UtilityFragment>
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

