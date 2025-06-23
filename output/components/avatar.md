# avatar

## Metadata
- **Version**: 0.0.1
- **Description**: Icons and/or text representing users or entities.
- **Category**: components

## Example Sections
1. **Small avatars**
   - Description: 
2. **Large avatars**
   - Description: 
3. **Custom avatars**
   - Description: 

## Examples
### Small image avatar
- **Section**: Small avatars
- **URL**: components/avatar/small-image-avatar
- **Tags**: 
```tsx
import { Avatar } from '@visa/nova-react';

/// This is the base url for where your site is deployed. `import.meta.env.BASE_URL` is the environment variable used to import the base url for Vite. Change this import to match your build tool's base url.
const BASE_URL = import.meta.env.BASE_URL;
const user = 'Alex Miller';

export const SmallImageAvatar = () => {
  return <Avatar alt={user} small tag="img" src={BASE_URL + '/alex-miller-stock.png'} />;
};

```

### Small initials avatar
- **Section**: Small avatars
- **URL**: components/avatar/small-initials-avatar
- **Tags**: 
```tsx
import { Avatar } from '@visa/nova-react';

const user = 'Alex Miller';
const userInitials = 'AM';

export const SmallInitialsAvatar = () => {
  return (
    <Avatar role="img" aria-label={user} small>
      {userInitials}
    </Avatar>
  );
};

```

### Small horizontal icon avatar
- **Section**: Small avatars
- **URL**: components/avatar/small-horizontal-icon-avatar
- **Tags**: 
```tsx
import { VisaAccountLow, VisaChevronDownLow, VisaChevronUpLow } from '@visa/nova-icons-react';
import { Avatar, Button, DropdownMenu, TabSuffix, Tab, UtilityFragment } from '@visa/nova-react';
import { CSSProperties, useState } from 'react';
import { offset, useClick, useFloating, useInteractions } from '@floating-ui/react';

export const SmallHorizontalIconAvatar = () => {
  const [accountMenuOpen, setAccountMenuOpen] = useState(false);

  const onToggleAccountMenu = () => setAccountMenuOpen(!accountMenuOpen);

  // TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
  const id = 'horizontal-advanced-nav';

  // For dropdown menu in the horizontal nav, we use floating UI to open it up
  const { context, floatingStyles, refs } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-start',
  });
  const { getReferenceProps, getFloatingProps } = useInteractions([useClick(context)]);

  return (
    <div style={{ blockSize: '175px' }}>
      <Tab tag="div">
        <Button
          aria-expanded={accountMenuOpen}
          aria-label="Alex Miller"
          element={<Avatar tag="button" />}
          buttonSize="large"
          colorScheme="tertiary"
          ref={refs.setReference}
          {...getReferenceProps({ onClick: onToggleAccountMenu })}
        >
          <VisaAccountLow />
          <TabSuffix element={accountMenuOpen ? <VisaChevronUpLow /> : <VisaChevronDownLow />} />
        </Button>
        {accountMenuOpen && (
          <UtilityFragment vFlex vFlexCol vPadding={4}>
            <DropdownMenu
              id={`${id}-account-menu`}
              ref={refs.setFloating}
              style={
                {
                  inlineSize: '180px',
                  maxInlineSize: '100%',
                  '--v-surface-padding': '8px',
                  ...floatingStyles,
                } as CSSProperties
              }
              {...getFloatingProps()}
            >
              <UtilityFragment vFlex vJustifyContent="start" vPaddingHorizontal={8} vPaddingVertical={11}>
                <Button buttonSize="large" colorScheme="tertiary" tag="a" href="./avatar">
                  L2 label 1
                </Button>
              </UtilityFragment>
              <UtilityFragment vFlex vJustifyContent="start" vPaddingHorizontal={8} vPaddingVertical={11}>
                <Button buttonSize="large" colorScheme="tertiary" tag="a" href="./avatar">
                  L2 label 2
                </Button>
              </UtilityFragment>
            </DropdownMenu>
          </UtilityFragment>
        )}
      </Tab>
    </div>
  );
};

```

### Small vertical icon avatar
- **Section**: Small avatars
- **URL**: components/avatar/small-vertical-icon-avatar
- **Tags**: 
```tsx
import { VisaAccountTiny, VisaChevronDownTiny } from '@visa/nova-icons-react';
import { Button, Nav, Tabs, Tab, TabSuffix } from '@visa/nova-react';
import { useState } from 'react';

export const SmallVerticalIconAvatar = () => {
  const [accountIsOpen, setAccountIsOpen] = useState(false);

  return (
    <Nav aria-label="Vertical nav with active page" orientation="vertical" tag="div">
      <Tabs orientation="vertical" tag="div">
        <Tab tag="div">
          <Button
            aria-expanded={accountIsOpen}
            aria-label="Alex Miller"
            buttonSize="large"
            colorScheme="tertiary"
            onClick={() => setAccountIsOpen(!accountIsOpen)}
          >
            <VisaAccountTiny />
            <TabSuffix element={<VisaChevronDownTiny />} />
          </Button>
        </Tab>
        {accountIsOpen && (
          <div>
            <Tab role="none">
              <Button
                aria-current="page"
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./nav">L2 label 1</a>}
                role="tab"
              />
            </Tab>
            <Tab role="none">
              <Button
                aria-selected="false"
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./nav">L2 label 2</a>}
                role="tab"
              />
            </Tab>
          </div>
        )}
      </Tabs>
    </Nav>
  );
};

```

### Large image avatar
- **Section**: Large avatars
- **URL**: components/avatar/large-image-avatar
- **Tags**: 
```tsx
import { Avatar } from '@visa/nova-react';

/// This is the base url for where your site is deployed. `import.meta.env.BASE_URL` is the environment variable used to import the base url for Vite. Change this import to match your build tool's base url.
const BASE_URL = import.meta.env.BASE_URL;
const user = 'Alex Miller';

export const LargeImageAvatar = () => {
  return <Avatar alt={user} tag="img" src={BASE_URL + '/alex-miller-stock.png'} />;
};

```

### Large initials avatar
- **Section**: Large avatars
- **URL**: components/avatar/large-initials-avatar
- **Tags**: 
```tsx
import { Avatar } from '@visa/nova-react';

const user = 'Alex Miller';
const userInitials = 'AM';

export const LargeInitialsAvatar = () => {
  return <Avatar role="img" aria-label={user}>{userInitials}</Avatar>;
};

```

### Large icon avatar
- **Section**: Large avatars
- **URL**: components/avatar/large-icon-avatar
- **Tags**: 
```tsx
import { Avatar } from '@visa/nova-react';
import { VisaAccountLow } from '@visa/nova-icons-react';

const user = 'Alex Miller';

export const LargeIconAvatar = () => {
  return (
    <Avatar aria-label={user} role="img">
      <VisaAccountLow />
    </Avatar>
  );
};

```

### Large ficticious brand avatar
- **Section**: Large avatars
- **URL**: components/avatar/fictitious-brand-avatar
- **Tags**: 
```tsx
import { CSSProperties } from 'react';
import { Avatar } from '@visa/nova-react';

export const FictitiousBrandAvatar = () => {
  return (
    <Avatar
      role="img"
      aria-label="Brand"
      className="fictitious-brand"
      style={
        {
          '--v-avatar-background': '#6ef2fb',
          '--v-avatar-foreground': 'var(--palette-default-text)',
          '--typography-body-2-font-weight': 800,
        } as CSSProperties
      }
    >
      B
    </Avatar>
  );
};

```

### Avatar as button
- **Section**: Custom avatars
- **URL**: components/avatar/avatar-as-button
- **Tags**: 
```tsx
import { Avatar, Button, Badge } from '@visa/nova-react';
import { VisaAccountLow } from '@visa/nova-icons-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'avatar-as-a-button';

export const AvatarAsButton = () => {
  return (
    <Button
      element={<Avatar tag="button" />}
      aria-label="Notifications"
      aria-describedby={`${id}-notifications-count`}
      buttonSize="large"
      colorScheme="tertiary"
    >
      <VisaAccountLow />
      <Badge id={`${id}-notifications-count`} tag="sup" badgeVariant="number">
        3
      </Badge>
    </Button>
  );
};

```

## Property Sections
### Avatar
- **Selector**: <Avatar />
- **Description**: Icons and/or text representing users or entities.

### TabSuffix
- **Selector**: <TabSuffix />
- **Description**: Utility class for positioning and styling elements at the end of tab components.

## Properties
### ref
- **Section**: Avatar
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### small
- **Section**: Avatar
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Small Avatar

### tag
- **Section**: Avatar
- **Type**: ElementType
- **Default**: span
- **Required**: false
- **Description**: Tag of Component

### element
- **Section**: TabSuffix
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with children)

### ref
- **Section**: TabSuffix
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

