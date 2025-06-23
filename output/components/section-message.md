# section-message

## Metadata
- **Version**: 0.0.1
- **Description**: Section-level messages providing information about the status of a page or action.
- **Category**: components

## Example Sections
1. **Informational section messages**
   - Description: 
2. **Success section messages**
   - Description: 
3. **Warning section messages**
   - Description: 
4. **Error section messages headline**
   - Description: 
5. **Subtle section messages headline**
   - Description: 

## Examples
### Empty informational section message
- **Section**: Informational section messages
- **URL**: components/section-message/empty-information-section-message
- **Tags**: docs
```tsx
import { SectionMessage } from '@visa/nova-react';

export const EmptyInformationSectionMessage = () => {
  return <SectionMessage />;
};

```

### Default informational section message
- **Section**: Informational section messages
- **URL**: components/section-message/default-information-section-message
- **Tags**: docs
```tsx
import {
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography,
  UtilityFragment
} from '@visa/nova-react';

export const DefaultInformationSectionMessage = () => {
  return (
    <SectionMessage>
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Informational section message with title
- **Section**: Informational section messages
- **URL**: components/section-message/title-information-section-message
- **Tags**: docs
```tsx
import {
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography,
  UtilityFragment
} from '@visa/nova-react';

export const TitleInformationSectionMessage = () => {
  return (
    <SectionMessage>
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography tag="h4" variant="body-2-bold">Informational title</Typography>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Informational section message with link
- **Section**: Informational section messages
- **URL**: components/section-message/link-information-section-message
- **Tags**: docs
```tsx
import {
  Link,
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography
} from '@visa/nova-react';

export const LinkInformationSectionMessage = () => {
  return (
    <SectionMessage>
      <SectionMessageIcon />
      <SectionMessageContent>
        <Typography className="v-mb-8">
          This is required text that describes the section message in more detail.
        </Typography>
        <Link href="./section-message">Destination label</Link>
      </SectionMessageContent>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Informational section message with button
- **Section**: Informational section messages
- **URL**: components/section-message/button-information-section-message
- **Tags**: docs
```tsx
import {
  Button,
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography
} from '@visa/nova-react';

export const ButtonInformationSectionMessage = () => {
  return (
    <SectionMessage>
      <SectionMessageIcon />
      <SectionMessageContent>
        <Typography className="v-mb-8">
          This is required text that describes the section message in more detail.
        </Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </SectionMessageContent>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Informational section message without close icon button
- **Section**: Informational section messages
- **URL**: components/section-message/persistent-information-section-message
- **Tags**: docs
```tsx
import { SectionMessage, SectionMessageContent, SectionMessageIcon, Typography, UtilityFragment } from '@visa/nova-react';

export const PersistentInformationSectionMessage = () => {
  return (
    <SectionMessage>
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
    </SectionMessage>
  );
};

```

### Empty success section message
- **Section**: Success section messages
- **URL**: components/section-message/empty-success-section-message
- **Tags**: docs
```tsx
import { SectionMessage } from '@visa/nova-react';

export const EmptySuccessSectionMessage = () => {
  return <SectionMessage messageType="success" />;
};

```

### Default success section message
- **Section**: Success section messages
- **URL**: components/section-message/default-success-section-message
- **Tags**: docs
```tsx
import {
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography,
  UtilityFragment
} from '@visa/nova-react';

export const DefaultSuccessSectionMessage = () => {
  return (
    <SectionMessage messageType="success">
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Success section message with title
- **Section**: Success section messages
- **URL**: components/section-message/title-success-section-message
- **Tags**: docs
```tsx
import {
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography,
  UtilityFragment
} from '@visa/nova-react';

export const TitleSuccessSectionMessage = () => {
  return (
    <SectionMessage messageType="success">
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography  tag="h4" variant="body-2-bold">Success title</Typography>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Success section message with link
- **Section**: Success section messages
- **URL**: components/section-message/link-success-section-message
- **Tags**: docs
```tsx
import {
  Link,
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography
} from '@visa/nova-react';

export const LinkSuccessSectionMessage = () => {
  return (
    <SectionMessage messageType="success">
      <SectionMessageIcon />
      <SectionMessageContent>
        <Typography className="v-mb-8">
          This is required text that describes the section message in more detail.
        </Typography>
        <Link href="./section-message">Destination label</Link>
      </SectionMessageContent>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Success section message with button
- **Section**: Success section messages
- **URL**: components/section-message/button-success-section-message
- **Tags**: docs
```tsx
import {
  Button,
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography
} from '@visa/nova-react';

export const ButtonSuccessSectionMessage = () => {
  return (
    <SectionMessage messageType="success">
      <SectionMessageIcon />
      <SectionMessageContent>
        <Typography className="v-mb-8">
          This is required text that describes the section message in more detail.
        </Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </SectionMessageContent>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Success section message without close icon button
- **Section**: Success section messages
- **URL**: components/section-message/persistent-success-section-message
- **Tags**: docs
```tsx
import { SectionMessage, SectionMessageContent, SectionMessageIcon, Typography, UtilityFragment } from '@visa/nova-react';

export const PersistentSuccessSectionMessage = () => {
  return (
    <SectionMessage messageType="success">
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
    </SectionMessage>
  );
};

```

### Empty warning section message
- **Section**: Warning section messages
- **URL**: components/section-message/empty-warning-section-message
- **Tags**: docs
```tsx
import { SectionMessage } from '@visa/nova-react';

export const EmptyWarningSectionMessage = () => {
  return <SectionMessage messageType="warning" />;
};

```

### Default warning section message
- **Section**: Warning section messages
- **URL**: components/section-message/default-warning-section-message
- **Tags**: docs
```tsx
import {
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography,
  UtilityFragment
} from '@visa/nova-react';

export const DefaultWarningSectionMessage = () => {
  return (
    <SectionMessage messageType="warning">
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Warning section message with title
- **Section**: Warning section messages
- **URL**: components/section-message/title-warning-section-message
- **Tags**: docs
```tsx
import {
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography,
  UtilityFragment
} from '@visa/nova-react';

export const TitleWarningSectionMessage = () => {
  return (
    <SectionMessage messageType="warning">
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography  tag="h4" variant="body-2-bold">Warning title</Typography>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Warning section message with link
- **Section**: Warning section messages
- **URL**: components/section-message/link-warning-section-message
- **Tags**: docs
```tsx
import {
  Link,
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography
} from '@visa/nova-react';

export const LinkWarningSectionMessage = () => {
  return (
    <SectionMessage messageType="warning">
      <SectionMessageIcon />
      <SectionMessageContent>
        <Typography className="v-mb-8">
          This is required text that describes the section message in more detail.
        </Typography>
        <Link href="./section-message">Destination label</Link>
      </SectionMessageContent>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Warning section message with button
- **Section**: Warning section messages
- **URL**: components/section-message/button-warning-section-message
- **Tags**: docs
```tsx
import {
  Button,
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography
} from '@visa/nova-react';

export const ButtonWarningSectionMessage = () => {
  return (
    <SectionMessage messageType="warning">
      <SectionMessageIcon />
      <SectionMessageContent>
        <Typography className="v-mb-8">
          This is required text that describes the section message in more detail.
        </Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </SectionMessageContent>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Warning section message without close icon button
- **Section**: Warning section messages
- **URL**: components/section-message/persistent-warning-section-message
- **Tags**: docs
```tsx
import { SectionMessage, SectionMessageContent, SectionMessageIcon, Typography, UtilityFragment } from '@visa/nova-react';

export const PersistentWarningSectionMessage = () => {
  return (
    <SectionMessage messageType="warning">
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
    </SectionMessage>
  );
};

```

### Empty error section message
- **Section**: Error section messages headline
- **URL**: components/section-message/empty-error-section-message
- **Tags**: docs
```tsx
import { SectionMessage } from '@visa/nova-react';

export const EmptyErrorSectionMessage = () => {
  return <SectionMessage messageType="error" />;
};

```

### Default error section message
- **Section**: Error section messages headline
- **URL**: components/section-message/default-error-section-message
- **Tags**: docs
```tsx
import {
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography,
  UtilityFragment
} from '@visa/nova-react';

export const DefaultErrorSectionMessage = () => {
  return (
    <SectionMessage messageType="error">
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Error section message with title
- **Section**: Error section messages headline
- **URL**: components/section-message/title-error-section-message
- **Tags**: docs
```tsx
import {
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography,
  UtilityFragment
} from '@visa/nova-react';

export const TitleErrorSectionMessage = () => {
  return (
    <SectionMessage messageType="error">
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography  tag="h4" variant="body-2-bold">Error title</Typography>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Error section message with link
- **Section**: Error section messages headline
- **URL**: components/section-message/link-error-section-message
- **Tags**: docs
```tsx
import {
  Link,
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography
} from '@visa/nova-react';

export const LinkErrorSectionMessage = () => {
  return (
    <SectionMessage messageType="error">
      <SectionMessageIcon />
      <SectionMessageContent>
        <Typography className="v-mb-8">
          This is required text that describes the section message in more detail.
        </Typography>
        <Link href="./section-message">Destination label</Link>
      </SectionMessageContent>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Error section message with button
- **Section**: Error section messages headline
- **URL**: components/section-message/button-error-section-message
- **Tags**: docs
```tsx
import {
  Button,
  SectionMessage,
  SectionMessageCloseButton,
  SectionMessageContent,
  SectionMessageIcon,
  Typography
} from '@visa/nova-react';

export const ButtonErrorSectionMessage = () => {
  return (
    <SectionMessage messageType="error">
      <SectionMessageIcon />
      <SectionMessageContent>
        <Typography className="v-mb-8">
          This is required text that describes the section message in more detail.
        </Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </SectionMessageContent>
      <SectionMessageCloseButton />
    </SectionMessage>
  );
};

```

### Error section message without close icon button
- **Section**: Error section messages headline
- **URL**: components/section-message/persistent-error-section-message
- **Tags**: docs
```tsx
import { SectionMessage, SectionMessageContent, SectionMessageIcon, Typography, UtilityFragment } from '@visa/nova-react';

export const PersistentErrorSectionMessage = () => {
  return (
    <SectionMessage messageType="error">
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
    </SectionMessage>
  );
};

```

### Empty subtle section message
- **Section**: Subtle section messages headline
- **URL**: components/section-message/empty-subtle-section-message
- **Tags**: 
```tsx
import { SectionMessage } from '@visa/nova-react';

export const EmptySubtleSectionMessage = () => {
  return <SectionMessage messageType="subtle" />;
};

```

### Default subtle section message
- **Section**: Subtle section messages headline
- **URL**: components/section-message/default-subtle-section-message
- **Tags**: 
```tsx
import {
    SectionMessage,
    SectionMessageCloseButton,
    SectionMessageContent,
    SectionMessageIcon,
    Typography,
    UtilityFragment
  } from '@visa/nova-react';
  
  export const DefaultSubtleSectionMessage = () => {
    return (
      <SectionMessage messageType="subtle">
        <SectionMessageIcon />
        <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
          <SectionMessageContent>
            <Typography>This is required text that describes the section message in more detail.</Typography>
          </SectionMessageContent>
        </UtilityFragment>
        <SectionMessageCloseButton />
      </SectionMessage>
    );
  };
  
```

### Subtle section message with title
- **Section**: Subtle section messages headline
- **URL**: components/section-message/title-subtle-section-message
- **Tags**: 
```tsx
import {
    SectionMessage,
    SectionMessageCloseButton,
    SectionMessageContent,
    SectionMessageIcon,
    Typography,
    UtilityFragment
  } from '@visa/nova-react';
  
  export const TitleSubtleSectionMessage = () => {
    return (
      <SectionMessage messageType="subtle">
        <SectionMessageIcon />
        <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
          <SectionMessageContent>
            <Typography  tag="h4" variant="body-2-bold">Error title</Typography>
            <Typography>This is required text that describes the section message in more detail.</Typography>
          </SectionMessageContent>
        </UtilityFragment>
        <SectionMessageCloseButton />
      </SectionMessage>
    );
  };
  
```

### Subtle section message with link
- **Section**: Subtle section messages headline
- **URL**: components/section-message/link-subtle-section-message
- **Tags**: 
```tsx
import {
    Link,
    SectionMessage,
    SectionMessageCloseButton,
    SectionMessageContent,
    SectionMessageIcon,
    Typography
  } from '@visa/nova-react';
  
  export const LinkSubtleSectionMessage = () => {
    return (
      <SectionMessage messageType="subtle">
        <SectionMessageIcon />
        <SectionMessageContent>
          <Typography className="v-mb-8">
            This is required text that describes the section message in more detail.
          </Typography>
          <Link href="./section-message">Destination label</Link>
        </SectionMessageContent>
        <SectionMessageCloseButton />
      </SectionMessage>
    );
  };
  
```

### Subtle section message with button
- **Section**: Subtle section messages headline
- **URL**: components/section-message/button-subtle-section-message
- **Tags**: 
```tsx
import {
    Button,
    SectionMessage,
    SectionMessageCloseButton,
    SectionMessageContent,
    SectionMessageIcon,
    Typography
  } from '@visa/nova-react';
  
  export const ButtonSubtleSectionMessage = () => {
    return (
      <SectionMessage messageType="subtle">
        <SectionMessageIcon />
        <SectionMessageContent>
          <Typography className="v-mb-8">
            This is required text that describes the section message in more detail.
          </Typography>
          <Button colorScheme="secondary">Primary action</Button>
        </SectionMessageContent>
        <SectionMessageCloseButton />
      </SectionMessage>
    );
  };
  
```

### Subtle section message without close icon button
- **Section**: Subtle section messages headline
- **URL**: components/section-message/persistent-subtle-section-message
- **Tags**: 
```tsx
import { SectionMessage, SectionMessageContent, SectionMessageIcon, Typography, UtilityFragment } from '@visa/nova-react';

export const PersistentSubtleSectionMessage = () => {
  return (
    <SectionMessage messageType="subtle">
      <SectionMessageIcon />
      <UtilityFragment vPaddingLeft={2} vPaddingBottom={2}>
        <SectionMessageContent>
          <Typography>This is required text that describes the section message in more detail.</Typography>
        </SectionMessageContent>
      </UtilityFragment>
    </SectionMessage>
  );
};

```

## Property Sections
### SectionMessage
- **Selector**: <SectionMessage />
- **Description**: Section-level messages providing information about the status of a page or action.

### SectionMessageCloseButton
- **Selector**: <SectionMessageCloseButton />
- **Description**: Close button for section message component.

### MessageContent
- **Selector**: <MessageContent />
- **Description**: Container for message content elements.

### MessageIcon
- **Selector**: <MessageIcon />
- **Description**: Icon to display within message content.

## Properties
### messageType
- **Section**: SectionMessage
- **Type**: "subtle" , "warning" , "error" , "success"
- **Default**: 
- **Required**: false
- **Description**: Message Type

### ref
- **Section**: SectionMessage
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: SectionMessage
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag of Component

### alternate
- **Section**: SectionMessageCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate color scheme

### buttonSize
- **Section**: SectionMessageCloseButton
- **Type**: "small" , "large"
- **Default**: 
- **Required**: false
- **Description**: Size of Button

### colorScheme
- **Section**: SectionMessageCloseButton
- **Type**: "secondary" , "tertiary"
- **Default**: 
- **Required**: false
- **Description**: Color Scheme of Button

### destructive
- **Section**: SectionMessageCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Destructive Button

### element
- **Section**: SectionMessageCloseButton
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### iconButton
- **Section**: SectionMessageCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Button

### iconTwoColor
- **Section**: SectionMessageCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Two Button

### ref
- **Section**: SectionMessageCloseButton
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### stacked
- **Section**: SectionMessageCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Stacked Button

### subtle
- **Section**: SectionMessageCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Subtle Button

### tag
- **Section**: SectionMessageCloseButton
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

