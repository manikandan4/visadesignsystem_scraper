# banner

## Metadata
- **Version**: 0.0.1
- **Description**: Messages indicating the global status of an application or website.
- **Category**: components

## Example Sections
1. **Informational banners**
   - Description: 
2. **Success banners**
   - Description: 
3. **Warning banners**
   - Description: 
4. **Error banners**
   - Description: 

## Examples
### Empty informational banner
- **Section**: Informational banners
- **URL**: components/banner/empty-information-banner
- **Tags**: docs
```tsx
import { Banner } from '@visa/nova-react';

export const EmptyInformationBanner = () => {
  return <Banner></Banner>;
};

```

### Default informational banner
- **Section**: Informational banners
- **URL**: components/banner/default-information-banner
- **Tags**: docs
```tsx
import { Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const DefaultInformationBanner = () => {
  return (
    <Banner>
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Informational banner with title
- **Section**: Informational banners
- **URL**: components/banner/title-information-banner
- **Tags**: docs
```tsx
import { Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const TitleInformationBanner = () => {
  return (
    <Banner>
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography variant="body-2-bold">Informational title</Typography>
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Informational banner with link
- **Section**: Informational banners
- **URL**: components/banner/link-information-banner
- **Tags**: docs
```tsx
import { Link, Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const LinkInformationBanner = () => {
  return (
    <Banner>
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography className="v-mb-8">This is required text that describes the banner in more detail.</Typography>
        <Link href="./banner">Destination label</Link>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Informational banner with button
- **Section**: Informational banners
- **URL**: components/banner/button-information-banner
- **Tags**: docs
```tsx
import { Button, Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const ButtonInformationBanner = () => {
  return (
    <Banner>
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography className="v-mb-8">This is required text that describes the banner in more detail.</Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Informational banner without close icon button
- **Section**: Informational banners
- **URL**: components/banner/persistent-information-banner
- **Tags**: docs
```tsx
import { Banner, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const PersistentInformationBanner = () => {
  return (
    <Banner>
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
    </Banner>
  );
};

```

### Empty success banner
- **Section**: Success banners
- **URL**: components/banner/empty-success-banner
- **Tags**: docs
```tsx
import { Banner } from '@visa/nova-react';

export const EmptySuccessBanner = () => {
  return <Banner messageType="success"></Banner>;
};

```

### Default success banner
- **Section**: Success banners
- **URL**: components/banner/default-success-banner
- **Tags**: docs
```tsx
import { Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const DefaultSuccessBanner = () => {
  return (
    <Banner messageType="success">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Success banner with title
- **Section**: Success banners
- **URL**: components/banner/title-success-banner
- **Tags**: docs
```tsx
import { Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const TitleSuccessBanner = () => {
  return (
    <Banner messageType="success">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography variant="body-2-bold">Success title</Typography>
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Success banner with link
- **Section**: Success banners
- **URL**: components/banner/link-success-banner
- **Tags**: docs
```tsx
import { Link, Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const LinkSuccessBanner = () => {
  return (
    <Banner messageType="success">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography className="v-mb-8">This is required text that describes the banner in more detail.</Typography>
        <Link href="./banner">Destination label</Link>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Success banner with button
- **Section**: Success banners
- **URL**: components/banner/button-success-banner
- **Tags**: docs
```tsx
import { Button, Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const ButtonSuccessBanner = () => {
  return (
    <Banner messageType="success">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography className="v-mb-8">This is required text that describes the banner in more detail.</Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Success banner without close icon button
- **Section**: Success banners
- **URL**: components/banner/persistent-success-banner
- **Tags**: docs
```tsx
import { Banner, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const PersistentSuccessBanner = () => {
  return (
    <Banner messageType="success">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
    </Banner>
  );
};

```

### Empty warning banner
- **Section**: Warning banners
- **URL**: components/banner/empty-warning-banner
- **Tags**: docs
```tsx
import { Banner } from '@visa/nova-react';

export const EmptyWarningBanner = () => {
  return <Banner messageType="warning"></Banner>;
};

```

### Default warning banner
- **Section**: Warning banners
- **URL**: components/banner/default-warning-banner
- **Tags**: docs
```tsx
import { Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const DefaultWarningBanner = () => {
  return (
    <Banner messageType="warning">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Warning banner with title
- **Section**: Warning banners
- **URL**: components/banner/title-warning-banner
- **Tags**: docs
```tsx
import { Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const TitleWarningBanner = () => {
  return (
    <Banner messageType="warning">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography variant="body-2-bold">Warning title</Typography>
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Warning banner with link
- **Section**: Warning banners
- **URL**: components/banner/link-warning-banner
- **Tags**: docs
```tsx
import { Link, Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const LinkWarningBanner = () => {
  return (
    <Banner messageType="warning">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography className="v-mb-8">This is required text that describes the banner in more detail.</Typography>
        <Link href="./banner">Destination label</Link>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Warning banner with button
- **Section**: Warning banners
- **URL**: components/banner/button-warning-banner
- **Tags**: docs
```tsx
import { Button, Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const ButtonWarningBanner = () => {
  return (
    <Banner messageType="warning">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography className="v-mb-8">This is required text that describes the banner in more detail.</Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Warning banner without close icon button
- **Section**: Warning banners
- **URL**: components/banner/persistent-warning-banner
- **Tags**: docs
```tsx
import { Banner, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const PersistentWarningBanner = () => {
  return (
    <Banner messageType="warning">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
    </Banner>
  );
};

```

### Empty error banner
- **Section**: Error banners
- **URL**: components/banner/empty-error-banner
- **Tags**: docs
```tsx
import { Banner } from '@visa/nova-react';

export const EmptyErrorBanner = () => {
  return <Banner messageType="error"></Banner>;
};

```

### Default error banner
- **Section**: Error banners
- **URL**: components/banner/default-error-banner
- **Tags**: docs
```tsx
import { Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const DefaultErrorBanner = () => {
  return (
    <Banner messageType="error">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Error banner with title
- **Section**: Error banners
- **URL**: components/banner/title-error-banner
- **Tags**: docs
```tsx
import { Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const TitleErrorBanner = () => {
  return (
    <Banner messageType="error">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography variant="body-2-bold">Error title</Typography>
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Error banner with link
- **Section**: Error banners
- **URL**: components/banner/link-error-banner
- **Tags**: docs
```tsx
import { Link, Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const LinkErrorBanner = () => {
  return (
    <Banner messageType="error">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography className="v-mb-8">This is required text that describes the banner in more detail.</Typography>
        <Link href="./banner">Destination label</Link>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Error banner with button
- **Section**: Error banners
- **URL**: components/banner/button-error-banner
- **Tags**: docs
```tsx
import { Button, Banner, BannerCloseButton, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const ButtonErrorBanner = () => {
  return (
    <Banner messageType="error">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography className="v-mb-8">This is required text that describes the banner in more detail.</Typography>
        <Button colorScheme="secondary">Primary action</Button>
      </BannerContent>
      <BannerCloseButton />
    </Banner>
  );
};

```

### Error banner without close icon button
- **Section**: Error banners
- **URL**: components/banner/persistent-error-banner
- **Tags**: docs
```tsx
import { Banner, BannerContent, BannerIcon, Typography } from '@visa/nova-react';

export const PersistentErrorBanner = () => {
  return (
    <Banner messageType="error">
      <BannerIcon />
      <BannerContent className="v-pl-2 v-pb-2">
        <Typography>This is required text that describes the banner in more detail.</Typography>
      </BannerContent>
    </Banner>
  );
};

```

## Property Sections
### Banner
- **Selector**: <Banner />
- **Description**: Messages indicating the global status of an application or website.

### BannerCloseButton
- **Selector**: <BannerCloseButton />
- **Description**: Close button used in upper corner of banner.

### MessageContent
- **Selector**: <MessageContent />
- **Description**: Container for message content elements.

### MessageIcon
- **Selector**: <MessageIcon />
- **Description**: Icon to display within message content.

## Properties
### messageType
- **Section**: Banner
- **Type**: "subtle" , "warning" , "error" , "success"
- **Default**: 
- **Required**: false
- **Description**: Message Type

### ref
- **Section**: Banner
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Banner
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag of Component

### alternate
- **Section**: BannerCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate color scheme

### buttonSize
- **Section**: BannerCloseButton
- **Type**: "small" , "large"
- **Default**: 
- **Required**: false
- **Description**: Size of Button

### colorScheme
- **Section**: BannerCloseButton
- **Type**: "secondary" , "tertiary"
- **Default**: 
- **Required**: false
- **Description**: Color Scheme of Button

### destructive
- **Section**: BannerCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Destructive Button

### element
- **Section**: BannerCloseButton
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### iconButton
- **Section**: BannerCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Button

### iconTwoColor
- **Section**: BannerCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Two Button

### ref
- **Section**: BannerCloseButton
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### stacked
- **Section**: BannerCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Stacked Button

### subtle
- **Section**: BannerCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Subtle Button

### tag
- **Section**: BannerCloseButton
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

