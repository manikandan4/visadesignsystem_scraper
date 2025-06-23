# flag

## Metadata
- **Version**: 0.0.1
- **Description**: Messages that provide low-priority updates about a process or event
- **Category**: components

## Example Sections
1. **Informational flags**
   - Description: 
2. **Success flags**
   - Description: 
3. **Warning flags**
   - Description: 
4. **Error flags**
   - Description: 

## Examples
### Empty informational flag
- **Section**: Informational flags
- **URL**: components/flag/empty-information-flag
- **Tags**: docs
```tsx
import { Flag } from '@visa/nova-react';

export const EmptyInformationFlag = () => {
  return <Flag />;
};

```

### Default informational flag
- **Section**: Informational flags
- **URL**: components/flag/default-information-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, ScreenReader } from '@visa/nova-react';

export const DefaultInformationFlag = () => {
  return (
    <Flag>
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
      <ScreenReader>information</ScreenReader>This is required text that describes the flag in more detail.</FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Informational flag with title
- **Section**: Informational flags
- **URL**: components/flag/title-information-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const TitleInformationFlag = () => {
  return (
    <Flag>
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>information</ScreenReader>
        <Typography variant="body-2-bold">Informational title</Typography>
        <Typography>This is required text that describes the flag in more detail.</Typography>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Informational flag with link
- **Section**: Informational flags
- **URL**: components/flag/link-information-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, Link, Typography, ScreenReader } from '@visa/nova-react';

export const LinkInformationFlag = () => {
  return (
    <Flag>
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>information</ScreenReader>
        <Typography className="v-mb-8">This is required text that describes the flag in more detail.</Typography>
        <Link href="./flag">Destination label</Link>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Informational flag with button
- **Section**: Informational flags
- **URL**: components/flag/button-information-flag
- **Tags**: docs
```tsx
import { Button, Flag, FlagCloseButton, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const ButtonInformationFlag = () => {
  return (
    <Flag>
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>information</ScreenReader>
        <Typography className="v-mb-8">This is required text that describes the flag in more detail.</Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Informational flag without close icon button
- **Section**: Informational flags
- **URL**: components/flag/persistent-information-flag
- **Tags**: docs
```tsx
import { Flag, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const PersistentInformationFlag = () => {
  return (
    <Flag>
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>information</ScreenReader>
        <Typography>This is required text that describes the flag in more detail.</Typography>
      </FlagContent>
    </Flag>
  );
};

```

### Empty success flag
- **Section**: Success flags
- **URL**: components/flag/empty-success-flag
- **Tags**: docs
```tsx
import { Flag } from '@visa/nova-react';

export const EmptySuccessFlag = () => {
  return <Flag messageType="success" />;
};

```

### Default success flag
- **Section**: Success flags
- **URL**: components/flag/default-success-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, ScreenReader } from '@visa/nova-react';

export const DefaultSuccessFlag = () => {
  return (
    <Flag messageType="success">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>success</ScreenReader>This is required text that describes the flag in more detail.
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Success flag with title
- **Section**: Success flags
- **URL**: components/flag/title-success-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const TitleSuccessFlag = () => {
  return (
    <Flag messageType="success">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>success</ScreenReader>
        <Typography variant="body-2-bold">Success title</Typography>
        <Typography>This is required text that describes the flag in more detail.</Typography>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Success flag with link
- **Section**: Success flags
- **URL**: components/flag/link-success-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, Link, Typography, ScreenReader } from '@visa/nova-react';

export const LinkSuccessFlag = () => {
  return (
    <Flag messageType="success">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>success</ScreenReader>
        <Typography className="v-mb-8">This is required text that describes the flag in more detail.</Typography>
        <Link href="./flag">Destination label</Link>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Success flag with button
- **Section**: Success flags
- **URL**: components/flag/button-success-flag
- **Tags**: docs
```tsx
import { Button, Flag, FlagCloseButton, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const ButtonSuccessFlag = () => {
  return (
    <Flag messageType="success">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>success</ScreenReader>
        <Typography className="v-mb-8">This is required text that describes the flag in more detail.</Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Success flag without close icon button
- **Section**: Success flags
- **URL**: components/flag/persistent-success-flag
- **Tags**: docs
```tsx
import { Flag, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const PersistentSuccessFlag = () => {
  return (
    <Flag messageType="success">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>success</ScreenReader>
        <Typography>This is required text that describes the flag in more detail.</Typography>
      </FlagContent>
    </Flag>
  );
};

```

### Empty warning flag
- **Section**: Warning flags
- **URL**: components/flag/empty-warning-flag
- **Tags**: docs
```tsx
import { Flag } from '@visa/nova-react';

export const EmptyWarningFlag = () => {
  return <Flag messageType="warning" />;
};

```

### Default warning flag
- **Section**: Warning flags
- **URL**: components/flag/default-warning-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, ScreenReader } from '@visa/nova-react';

export const DefaultWarningFlag = () => {
  return (
    <Flag messageType="warning">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>warning</ScreenReader>This is required text that describes the flag in more detail.</FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Warning flag with title
- **Section**: Warning flags
- **URL**: components/flag/title-warning-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const TitleWarningFlag = () => {
  return (
    <Flag messageType="warning">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>warning</ScreenReader>
        <Typography variant="body-2-bold">Warning title</Typography>
        <Typography>This is required text that describes the flag in more detail.</Typography>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Warning flag with link
- **Section**: Warning flags
- **URL**: components/flag/link-warning-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, Link, Typography, ScreenReader } from '@visa/nova-react';

export const LinkWarningFlag = () => {
  return (
    <Flag messageType="warning">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>warning</ScreenReader>
        <Typography className="v-mb-8">This is required text that describes the flag in more detail.</Typography>
        <Link href="./flag">Destination label</Link>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Warning flag with button
- **Section**: Warning flags
- **URL**: components/flag/button-warning-flag
- **Tags**: docs
```tsx
import { Button, Flag, FlagCloseButton, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const ButtonWarningFlag = () => {
  return (
    <Flag messageType="warning">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>warning</ScreenReader>
        <Typography className="v-mb-8">This is required text that describes the flag in more detail.</Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Warning flag without close icon button
- **Section**: Warning flags
- **URL**: components/flag/persistent-warning-flag
- **Tags**: docs
```tsx
import { Flag, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const PersistentWarningFlag = () => {
  return (
    <Flag messageType="warning">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>warning</ScreenReader>
        <Typography>This is required text that describes the flag in more detail.</Typography>
      </FlagContent>
    </Flag>
  );
};

```

### Empty error flag
- **Section**: Error flags
- **URL**: components/flag/empty-error-flag
- **Tags**: docs
```tsx
import { Flag } from '@visa/nova-react';

export const EmptyErrorFlag = () => {
  return <Flag messageType="error" />;
};

```

### Default error flag
- **Section**: Error flags
- **URL**: components/flag/default-error-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, ScreenReader } from '@visa/nova-react';

export const DefaultErrorFlag = () => {
  return (
    <Flag messageType="error">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>error</ScreenReader>
        This is required text that describes the flag in more detail.</FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Error flag with title
- **Section**: Error flags
- **URL**: components/flag/title-error-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const TitleErrorFlag = () => {
  return (
    <Flag messageType="error">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>error</ScreenReader>
        <Typography variant="body-2-bold">Error title</Typography>
        <Typography>This is required text that describes the flag in more detail.</Typography>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Error flag with link
- **Section**: Error flags
- **URL**: components/flag/link-error-flag
- **Tags**: docs
```tsx
import { Flag, FlagCloseButton, FlagContent, FlagIcon, Link, Typography, ScreenReader } from '@visa/nova-react';

export const LinkErrorFlag = () => {
  return (
    <Flag messageType="error">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>error</ScreenReader>
        <Typography className="v-mb-8">This is required text that describes the flag in more detail.</Typography>
        <Link href="./flag">Destination label</Link>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Error flag with button
- **Section**: Error flags
- **URL**: components/flag/button-error-flag
- **Tags**: docs
```tsx
import { Button, Flag, FlagCloseButton, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const ButtonErrorFlag = () => {
  return (
    <Flag messageType="error">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>error</ScreenReader>
        <Typography className="v-mb-8">This is required text that describes the flag in more detail.</Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </FlagContent>
      <FlagCloseButton />
    </Flag>
  );
};

```

### Error flag without close icon button
- **Section**: Error flags
- **URL**: components/flag/persistent-error-flag
- **Tags**: docs
```tsx
import { Flag, FlagContent, FlagIcon, Typography, ScreenReader } from '@visa/nova-react';

export const PersistentErrorFlag = () => {
  return (
    <Flag messageType="error">
      <FlagIcon />
      <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
        <ScreenReader>error</ScreenReader>
        <Typography>This is required text that describes the flag in more detail.</Typography>
      </FlagContent>
    </Flag>
  );
};

```

## Property Sections
### Flag
- **Selector**: <Flag />
- **Description**: Messages that provide low-priority updates about a process or event

### FlagCloseButton
- **Selector**: <FlagCloseButton />
- **Description**: Close button to dismiss a flag message.

### MessageContent
- **Selector**: <MessageContent />
- **Description**: Container for message content elements.

### MessageIcon
- **Selector**: <MessageIcon />
- **Description**: Icon to display within message content.

## Properties
### messageType
- **Section**: Flag
- **Type**: "subtle" , "warning" , "error" , "success"
- **Default**: 
- **Required**: false
- **Description**: Message Type

### ref
- **Section**: Flag
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Flag
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag of Component

### alternate
- **Section**: FlagCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate color scheme

### buttonSize
- **Section**: FlagCloseButton
- **Type**: "small" , "large"
- **Default**: 
- **Required**: false
- **Description**: Size of Button

### colorScheme
- **Section**: FlagCloseButton
- **Type**: "secondary" , "tertiary"
- **Default**: 
- **Required**: false
- **Description**: Color Scheme of Button

### destructive
- **Section**: FlagCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Destructive Button

### element
- **Section**: FlagCloseButton
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### iconButton
- **Section**: FlagCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Button

### iconTwoColor
- **Section**: FlagCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Two Button

### ref
- **Section**: FlagCloseButton
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### stacked
- **Section**: FlagCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Stacked Button

### subtle
- **Section**: FlagCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Subtle Button

### tag
- **Section**: FlagCloseButton
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag (not compatible with element property)

### ref
- **Section**: MessageContent
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: MessageContent
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### element
- **Section**: MessageIcon
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element

### ref
- **Section**: MessageIcon
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

