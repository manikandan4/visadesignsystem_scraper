# button

## Metadata
- **Version**: 0.0.1
- **Description**: Interactive elements enabling users to take actions within an interface.
- **Category**: components

## Example Sections
1. **Primary text buttons**
   - Description: 
2. **Secondary text buttons**
   - Description: 
3. **Tertiary text buttons**
   - Description: 
4. **Destructive text buttons**
   - Description: 
5. **Primary icon buttons**
   - Description: 
6. **Secondary icon buttons**
   - Description: 
7. **UI icon buttons**
   - Description: 
8. **Stacked icon buttons**
   - Description: 
9. **Button coded as a link**
   - Description: 

## Examples
### Default primary text button
- **Section**: Primary text buttons
- **URL**: components/button/default-button
- **Tags**: 
```tsx
import { Button } from '@visa/nova-react';

export const DefaultButton = () => {
  return <Button>Primary action</Button>;
};

```

### Alternate primary text button
- **Section**: Primary text buttons
- **URL**: components/button/alternate-button
- **Tags**: 
```tsx
import { Button } from '@visa/nova-react';

export const AlternateButton = () => {
  return <Button alternate>Primary action</Button>;
};

```

### Primary text button with leading icon
- **Section**: Primary text buttons
- **URL**: components/button/with-leading-icon-button
- **Tags**: 
```tsx
import { VisaFileUploadTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const WithLeadingIconButton = () => {
  return (
    <Button iconTwoColor>
      <VisaFileUploadTiny />
      Primary action
    </Button>
  );
};

```

### Primary text button with trailing icon
- **Section**: Primary text buttons
- **URL**: components/button/with-trailing-icon-button
- **Tags**: 
```tsx
import { VisaFileUploadTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const WithTrailingIconButton = () => {
  return (
    <Button iconTwoColor>
      Primary action
      <VisaFileUploadTiny />
    </Button>
  );
};

```

### Disabled primary text button
- **Section**: Primary text buttons
- **URL**: components/button/disabled-button
- **Tags**: 
```tsx
import { VisaFileUploadTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const DisabledButton = () => {
  return (
    <Button disabled>
      <VisaFileUploadTiny />
      Primary action
    </Button>
  );
};

```

### Small primary text button
- **Section**: Primary text buttons
- **URL**: components/button/small-button
- **Tags**: 
```tsx
import { VisaFileUploadTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const SmallButton = () => {
  return (
    <Button buttonSize="small" iconTwoColor>
      <VisaFileUploadTiny />
      Primary action
    </Button>
  );
};

```

### Large primary text button
- **Section**: Primary text buttons
- **URL**: components/button/large-button
- **Tags**: 
```tsx
import { VisaFileUploadTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const LargeButton = () => {
  return (
    <Button buttonSize="large" iconTwoColor>
      <VisaFileUploadTiny />
      Primary action
    </Button>
  );
};

```

### Default secondary text button
- **Section**: Secondary text buttons
- **URL**: components/button/secondary-button
- **Tags**: 
```tsx
import { Button } from '@visa/nova-react';

export const SecondaryButton = () => {
  return <Button colorScheme="secondary">Secondary action</Button>;
};

```

### Alternate secondary text button
- **Section**: Secondary text buttons
- **URL**: components/button/alternate-secondary-button
- **Tags**: 
```tsx
import { Button } from '@visa/nova-react';

export const AlternateSecondaryButton = () => {
  return (
    <Button alternate colorScheme="secondary">
      Secondary action
    </Button>
  );
};

```

### Secondary text button with leading icon
- **Section**: Secondary text buttons
- **URL**: components/button/with-leading-icon-secondary-button
- **Tags**: 
```tsx
import { VisaSaveTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const WithLeadingIconSecondaryButton = () => {
  return (
    <Button colorScheme="secondary">
      <VisaSaveTiny />
      Secondary action
    </Button>
  );
};

```

### Secondary text button with trailing icon
- **Section**: Secondary text buttons
- **URL**: components/button/with-trailing-icon-secondary-button
- **Tags**: 
```tsx
import { VisaSaveTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const WithTrailingIconSecondaryButton = () => {
  return (
    <Button colorScheme="secondary">
      Secondary action
      <VisaSaveTiny />
    </Button>
  );
};

```

### Disabled secondary text button
- **Section**: Secondary text buttons
- **URL**: components/button/disabled-secondary-button
- **Tags**: 
```tsx
import { VisaSaveTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const DisabledSecondaryButton = () => {
  return (
    <Button colorScheme="secondary" disabled>
      <VisaSaveTiny />
      Secondary action
    </Button>
  );
};

```

### Small secondary text button
- **Section**: Secondary text buttons
- **URL**: components/button/small-secondary-button
- **Tags**: 
```tsx
import { VisaSaveTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const SmallSecondaryButton = () => {
  return (
    <Button buttonSize="small" colorScheme="secondary">
      <VisaSaveTiny />
      Secondary action
    </Button>
  );
};

```

### Large secondary text button
- **Section**: Secondary text buttons
- **URL**: components/button/large-secondary-button
- **Tags**: 
```tsx
import { VisaSaveTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const LargeSecondaryButton = () => {
  return (
    <Button buttonSize="large" colorScheme="secondary">
      <VisaSaveTiny />
      Secondary action
    </Button>
  );
};

```

### Default tertiary text button
- **Section**: Tertiary text buttons
- **URL**: components/button/tertiary-button
- **Tags**: 
```tsx
import { Button } from '@visa/nova-react';

export const TertiaryButton = () => {
  return <Button colorScheme="tertiary">Tertiary action</Button>;
};

```

### Alternate tertiary text button
- **Section**: Tertiary text buttons
- **URL**: components/button/alternate-tertiary-button
- **Tags**: 
```tsx
import { Button } from '@visa/nova-react';

export const AlternateTertiaryButton = () => {
  return (
    <Button alternate colorScheme="tertiary">
      Tertiary action
    </Button>
  );
};

```

### Tertiary text button with leading icon
- **Section**: Tertiary text buttons
- **URL**: components/button/with-leading-icon-tertiary-button
- **Tags**: 
```tsx
import { VisaHistoryTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const WithLeadingIconTertiaryButton = () => {
  return (
    <Button colorScheme="tertiary">
      <VisaHistoryTiny />
      Tertiary action
    </Button>
  );
};

```

### Tertiary text button with trailing icon
- **Section**: Tertiary text buttons
- **URL**: components/button/with-trailing-icon-tertiary-button
- **Tags**: 
```tsx
import { VisaHistoryTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const WithTrailingIconTertiaryButton = () => {
  return (
    <Button colorScheme="tertiary">
      Tertiary action
      <VisaHistoryTiny />
    </Button>
  );
};

```

### Disabled tertiary text button
- **Section**: Tertiary text buttons
- **URL**: components/button/disabled-tertiary-button
- **Tags**: 
```tsx
import { VisaHistoryTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const DisabledTertiaryButton = () => {
  return (
    <Button colorScheme="tertiary" disabled>
      <VisaHistoryTiny />
      Tertiary action
    </Button>
  );
};

```

### Small tertiary text button
- **Section**: Tertiary text buttons
- **URL**: components/button/small-tertiary-button
- **Tags**: 
```tsx
import { VisaHistoryTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const SmallTertiaryButton = () => {
  return (
    <Button buttonSize="small" colorScheme="tertiary">
      <VisaHistoryTiny />
      Tertiary action
    </Button>
  );
};

```

### Large tertiary text button
- **Section**: Tertiary text buttons
- **URL**: components/button/large-tertiary-button
- **Tags**: 
```tsx
import { VisaHistoryTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const LargeTertiaryButton = () => {
  return (
    <Button buttonSize="large" colorScheme="tertiary">
      <VisaHistoryTiny />
      Tertiary action
    </Button>
  );
};

```

### Primary destructive text button
- **Section**: Destructive text buttons
- **URL**: components/button/destructive-button
- **Tags**: 
```tsx
import { VisaDeleteTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const DestructiveButton = () => {
  return (
    <Button destructive>
      <VisaDeleteTiny />
      Destructive action
    </Button>
  );
};

```

### Secondary destructive text button
- **Section**: Destructive text buttons
- **URL**: components/button/destructive-secondary-button
- **Tags**: 
```tsx
import { VisaDeleteTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const DestructiveSecondaryButton = () => {
  return (
    <Button destructive colorScheme="secondary">
      <VisaDeleteTiny />
      Destructive action
    </Button>
  );
};

```

### Tertiary destructive text button
- **Section**: Destructive text buttons
- **URL**: components/button/destructive-tertiary-button
- **Tags**: 
```tsx
import { VisaDeleteTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const DestructiveTertiaryButton = () => {
  return (
    <Button colorScheme="tertiary" destructive>
      <VisaDeleteTiny />
      Destructive action
    </Button>
  );
};

```

### Default primary icon button
- **Section**: Primary icon buttons
- **URL**: components/button/icon-button
- **Tags**: 
```tsx
import { VisaAddTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const IconButton = () => {
  return (
    <Button aria-label="action" iconButton>
      <VisaAddTiny />
    </Button>
  );
};

```

### Alternate primary icon button
- **Section**: Primary icon buttons
- **URL**: components/button/icon-alternate-button
- **Tags**: 
```tsx
import { VisaAddTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const IconAlternateButton = () => {
  return (
    <Button alternate aria-label="action" iconButton>
      <VisaAddTiny />
    </Button>
  );
};

```

### Primary icon button with label
- **Section**: Primary icon buttons
- **URL**: components/button/with-label-icon-button
- **Tags**: 
```tsx
import { VisaAddTiny } from '@visa/nova-icons-react';
import { Button, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'icon-button';

export const WithLabelIconButton = () => {
  return (
    <Utility vFlex vFlexRow>
      <Utility vAlignItems="center" vFlex vFlexCol vGap={2}>
        <Button aria-labelledby={`${id}-label`} iconButton>
          <VisaAddTiny />
        </Button>
        <Typography id={`${id}-label`} tag="span" variant="label-small">
          Action
        </Typography>
      </Utility>
    </Utility>
  );
};

```

### Disabled primary icon button
- **Section**: Primary icon buttons
- **URL**: components/button/disabled-icon-button
- **Tags**: 
```tsx
import { VisaAddTiny } from '@visa/nova-icons-react';
import { Button, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-icon-button';

export const DisabledIconButton = () => {
  return (
    <Utility vFlex vFlexRow>
      <Utility vAlignItems="center" vFlex vFlexCol vGap={2}>
        <Button aria-labelledby={`${id}-label`} disabled iconButton>
          <VisaAddTiny />
        </Button>
        <Typography
          id={`${id}-label`}
          style={{ color: 'var(--palette-default-disabled)' }}
          tag="span"
          variant="label-small"
        >
          Action
        </Typography>
      </Utility>
    </Utility>
  );
};

```

### Small primary icon button
- **Section**: Primary icon buttons
- **URL**: components/button/small-icon-button
- **Tags**: 
```tsx
import { VisaAddTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const SmallIconButton = () => {
  return (
    <Button aria-label="action" buttonSize="small" iconButton iconTwoColor>
      <VisaAddTiny />
    </Button>
  );
};

```

### Large primary icon button
- **Section**: Primary icon buttons
- **URL**: components/button/large-icon-button
- **Tags**: 
```tsx
import { VisaAddLow } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const LargeIconButton = () => {
  return (
    <Button aria-label="action" buttonSize="large" iconButton iconTwoColor>
      <VisaAddLow />
    </Button>
  );
};

```

### Default secondary icon button
- **Section**: Secondary icon buttons
- **URL**: components/button/secondary-icon-button
- **Tags**: 
```tsx
import { VisaConnectTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const SecondaryIconButton = () => {
  return (
    <Button aria-label="action" colorScheme="secondary" iconButton>
      <VisaConnectTiny rtl />
    </Button>
  );
};

```

### Alternate secondary icon button
- **Section**: Secondary icon buttons
- **URL**: components/button/secondary-alternate-icon-button
- **Tags**: 
```tsx
import { VisaConnectTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const SecondaryAlternateIconButton = () => {
  return (
    <Button alternate aria-label="action" colorScheme="secondary" iconButton>
      <VisaConnectTiny rtl />
    </Button>
  );
};

```

### Secondary icon button with label
- **Section**: Secondary icon buttons
- **URL**: components/button/with-label-secondary-icon-button
- **Tags**: 
```tsx
import { VisaConnectTiny } from '@visa/nova-icons-react';
import { Button, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'secondary-icon-button';

export const WithLabelSecondaryIconButton = () => {
  return (
    <Utility vFlex vFlexRow>
      <Utility vAlignItems="center" vFlex vFlexCol vGap={2}>
        <Button aria-labelledby={`${id}-label`} colorScheme="secondary" iconButton>
          <VisaConnectTiny rtl />
        </Button>
        <Typography id={`${id}-label`} tag="span" variant="label-small">
          Action
        </Typography>
      </Utility>
    </Utility>
  );
};

```

### Disabled secondary icon button
- **Section**: Secondary icon buttons
- **URL**: components/button/disabled-secondary-icon-button
- **Tags**: 
```tsx
import { VisaConnectTiny } from '@visa/nova-icons-react';
import { Button, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-secondary-icon-button';

export const DisabledSecondaryIconButton = () => {
  return (
    <Utility vFlex vFlexRow>
      <Utility vAlignItems="center" vFlex vFlexCol>
        <Button aria-labelledby={`${id}-label`} colorScheme="secondary" disabled iconButton>
          <VisaConnectTiny rtl />
        </Button>
        <Typography
          id={`${id}-label`}
          style={{ color: 'var(--palette-default-disabled)' }}
          tag="span"
          variant="label-small"
        >
          Action
        </Typography>
      </Utility>
    </Utility>
  );
};

```

### Large secondary icon button
- **Section**: Secondary icon buttons
- **URL**: components/button/large-secondary-icon-button
- **Tags**: 
```tsx
import { VisaConnectLow } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const LargeSecondaryIconButton = () => {
  return (
    <Button aria-label="action" buttonSize="large" colorScheme="secondary" iconButton>
      <VisaConnectLow rtl />
    </Button>
  );
};

```

### Small UI icon button
- **Section**: UI icon buttons
- **URL**: components/button/small-ui-icon-button
- **Tags**: 
```tsx
import { VisaNotificationsTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const SmallUiIconButton = () => {
  return (
    <Button aria-label="action" buttonSize="small" colorScheme="tertiary" iconButton>
      <VisaNotificationsTiny />
    </Button>
  );
};

```

### Medium UI icon button
- **Section**: UI icon buttons
- **URL**: components/button/ui-icon-button
- **Tags**: 
```tsx
import { VisaNotificationsTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const UiIconButton = () => {
  return (
    <Button aria-label="action" colorScheme="tertiary" iconButton>
      <VisaNotificationsTiny />
    </Button>
  );
};

```

### Large UI icon button
- **Section**: UI icon buttons
- **URL**: components/button/large-ui-icon-button
- **Tags**: 
```tsx
import { VisaNotificationsLow } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const LargeUiIconButton = () => {
  return (
    <Button aria-label="action" buttonSize="large" colorScheme="tertiary" iconButton>
      <VisaNotificationsLow />
    </Button>
  );
};

```

### Subtle UI icon button
- **Section**: UI icon buttons
- **URL**: components/button/subtle-ui-icon-button
- **Tags**: 
```tsx
import { VisaNotificationsTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const SubtleUiIconButton = () => {
  return (
    <Button aria-label="action" colorScheme="tertiary" iconButton subtle>
      <VisaNotificationsTiny />
    </Button>
  );
};

```

### UI icon button with badge
- **Section**: UI icon buttons
- **URL**: components/button/with-badge-number-ui-icon-button
- **Tags**: 
```tsx
import { VisaNotificationsTiny } from '@visa/nova-icons-react';
import { Badge, Button } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'with-badge-number-ui-icon-button';

export const WithBadgeNumberUiIconButton = () => {
  return (
    <Button aria-describedby={`${id}-badge`} buttonSize="large" colorScheme="tertiary" iconButton>
      <VisaNotificationsTiny />
      <Badge aria-label="9 unread notifications" badgeVariant="number" id={`${id}-badge`} tag="sup">
        9
      </Badge>
    </Button>
  );
};

```

### Alternate UI icon button
- **Section**: UI icon buttons
- **URL**: components/button/alternate-ui-icon-button
- **Tags**: 
```tsx
import { VisaNotificationsTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const AlternateUiIconButton = () => {
  return (
    <Button alternate aria-label="action" colorScheme="tertiary" iconButton>
      <VisaNotificationsTiny />
    </Button>
  );
};

```

### Default stacked icon button
- **Section**: Stacked icon buttons
- **URL**: components/button/stacked-icon-button
- **Tags**: 
```tsx
import { VisaGlossaryLow } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const StackedIconButton = () => {
  return (
    <Button colorScheme="tertiary" stacked>
      <VisaGlossaryLow />
      Action
    </Button>
  );
};

```

### Alternate stacked icon button
- **Section**: Stacked icon buttons
- **URL**: components/button/alternate-stacked-icon-button
- **Tags**: 
```tsx
import { VisaGlossaryLow } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const AlternateStackedIconButton = () => {
  return (
    <Button alternate colorScheme="tertiary" stacked>
      <VisaGlossaryLow />
      Action
    </Button>
  );
};

```

### Button coded as a link
- **Section**: Button coded as a link
- **URL**: components/button/coded-as-link-button
- **Tags**: 
```tsx
import { VisaChevronRightTiny } from '@visa/nova-icons-react';
import { Button } from '@visa/nova-react';

export const CodedAsLinkButton = () => {
  return (
    <Button
      element={
        <a href="./button">
          Primary action
          <VisaChevronRightTiny rtl />
        </a>
      }
    />
  );
};

```

## Property Sections
### Button
- **Selector**: <Button />
- **Description**: Interactive elements enabling users to take actions within an interface.

## Properties
### alternate
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate color scheme

### buttonSize
- **Section**: Button
- **Type**: "small" , "large"
- **Default**: 
- **Required**: false
- **Description**: Size of Button

### colorScheme
- **Section**: Button
- **Type**: "secondary" , "tertiary"
- **Default**: 
- **Required**: false
- **Description**: Color Scheme of Button

### destructive
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Destructive Button

### element
- **Section**: Button
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### iconButton
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Button

### iconTwoColor
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Two Button

### ref
- **Section**: Button
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### stacked
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Stacked Button

### subtle
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Subtle Button

### tag
- **Section**: Button
- **Type**: ElementType
- **Default**: button
- **Required**: false
- **Description**: Tag (not compatible with element property)

