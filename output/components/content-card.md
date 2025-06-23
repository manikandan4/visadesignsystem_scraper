# content-card

## Metadata
- **Version**: 0.0.1
- **Description**: Compact displays summarizing or directing users to more information.
- **Category**: components

## Example Sections
1. **Default content cards**
   - Description: 
2. **Dashboard content cards**
   - Description: 

## Examples
### Default content card
- **Section**: Default content cards
- **URL**: components/content-card/default-content-card
- **Tags**: 
```tsx
import { VisaChevronRightTiny } from '@visa/nova-icons-react';
import {
  Button,
  ContentCard,
  ContentCardBody,
  ContentCardSubtitle,
  ContentCardTitle,
  Link,
  Typography,
  Utility,
} from '@visa/nova-react';

export const DefaultContentCard = () => {
  return (
    <ContentCard>
      <Utility element={<ContentCardBody />} vFlex vFlexCol vGap={4}>
        <ContentCardTitle variant="headline-4">Headline</ContentCardTitle>
        <ContentCardSubtitle variant="subtitle-3">Subtitle</ContentCardSubtitle>
        <Typography className="v-pt-4">
          This is optional text that describes the headline and subtitle in more detail.
        </Typography>
        <Utility vAlignItems="center" vFlex vFlexWrap vGap={16} vPaddingTop={12}>
          <Button>Primary action</Button>
          <Link href="./content-card" noUnderline>
            Destination label <VisaChevronRightTiny rtl />
          </Link>
        </Utility>
      </Utility>
    </ContentCard>
  );
};

```

### Content card with UI buttons
- **Section**: Default content cards
- **URL**: components/content-card/with-buttons-content-card
- **Tags**: 
```tsx
import { VisaChevronRightTiny, VisaFileUploadTiny } from '@visa/nova-icons-react';
import {
  Button,
  ContentCard,
  ContentCardBody,
  ContentCardSubtitle,
  ContentCardTitle,
  Link,
  Typography,
  Utility,
} from '@visa/nova-react';

export const WithButtonsContentCard = () => {
  return (
    <ContentCard>
      <Utility element={<ContentCardBody />} vFlex vFlexCol vGap={4}>
        <Utility vAlignItems="center" vFlex vFlexRow vJustifyContent="between">
          <ContentCardTitle variant="headline-4">Headline</ContentCardTitle>
          <Button aria-label="Export [Headline]" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaFileUploadTiny />
          </Button>
        </Utility>
        <ContentCardSubtitle variant="subtitle-3">Subtitle</ContentCardSubtitle>
        <Typography className="v-pt-4">
          This is optional text that describes the headline and subtitle in more detail.
        </Typography>
        <Utility vAlignItems="center" vFlex vFlexWrap vGap={16} vPaddingTop={12}>
          <Button>Primary action</Button>
          <Link href="./content-card" noUnderline>
            Destination label <VisaChevronRightTiny rtl />
          </Link>
        </Utility>
      </Utility>
    </ContentCard>
  );
};

```

### Clickable content card
- **Section**: Default content cards
- **URL**: components/content-card/clickable-content-card
- **Tags**: 
```tsx
import { VisaChevronRightTiny } from '@visa/nova-icons-react';
import {
  ContentCard,
  ContentCardBody,
  ContentCardSubtitle,
  ContentCardTitle,
  Typography,
  Utility,
} from '@visa/nova-react';

export const ClickableContentCard = () => {
  return (
    <ContentCard clickable tag="button">
      <Utility element={<ContentCardBody tag="span" />} vAlignItems="start" vFlex vFlexCol vGap={4}>
        <ContentCardTitle variant="headline-4" tag="span">
          Headline
          <VisaChevronRightTiny rtl className="v-icon-move" />
        </ContentCardTitle>
        <ContentCardSubtitle variant="subtitle-3" tag="span">
          Subtitle
        </ContentCardSubtitle>
        <Utility element={<Typography tag="span" />} vPaddingTop={4}>
          This is optional text that describes the headline in more detail.
        </Utility>
      </Utility>
    </ContentCard>
  );
};

```

### Disabled clickable content card
- **Section**: Default content cards
- **URL**: components/content-card/clickable-disabled-content-card
- **Tags**: 
```tsx
import { VisaSecurityLockTiny } from '@visa/nova-icons-react';
import {
  ContentCard,
  ContentCardBody,
  ContentCardSubtitle,
  ContentCardTitle,
  Typography,
  Utility,
} from '@visa/nova-react';

export const ClickableDisabledContentCard = () => {
  return (
    <ContentCard aria-disabled="true" clickable tag="button" disabled>
      <Utility element={<ContentCardBody />} vFlex vFlexCol vGap={4}>
        <Utility vAlignItems="center" vFlex vGap={12}>
          <ContentCardTitle variant="headline-4" tag="span">
            Headline
          </ContentCardTitle>
          <VisaSecurityLockTiny />
        </Utility>
        <ContentCardSubtitle variant="subtitle-3" tag="span">
          Subtitle
        </ContentCardSubtitle>
        <Typography className="v-pt-4" tag="span">
          This is optional text that describes the headline in more detail.
        </Typography>
      </Utility>
    </ContentCard>
  );
};

```

### Compact content card
- **Section**: Default content cards
- **URL**: components/content-card/compact-content-card
- **Tags**: 
```tsx
import { VisaChevronRightTiny } from '@visa/nova-icons-react';
import { ContentCard, ContentCardBody, ContentCardSubtitle, ContentCardTitle, Link, Utility } from '@visa/nova-react';

export const CompactContentCard = () => {
  return (
    <ContentCard borderBlockEnd>
      <Utility element={<ContentCardBody />} vFlex vFlexCol vGap={10}>
        <ContentCardTitle variant="headline-4">Headline</ContentCardTitle>
        <ContentCardSubtitle className="v-pt-4" variant="body-2">
          This is optional text that describes the headline and subtitle in more detail.
        </ContentCardSubtitle>
        <Utility vPaddingTop={12}>
          <Link href="./content-card" noUnderline>
            Destination label <VisaChevronRightTiny rtl />
          </Link>
        </Utility>
      </Utility>
    </ContentCard>
  );
};

```

### Content card with category
- **Section**: Default content cards
- **URL**: components/content-card/category-content-card
- **Tags**: 
```tsx
import { VisaAccountLow, VisaChevronRightTiny } from '@visa/nova-icons-react';
import {
  Button,
  ContentCard,
  ContentCardBody,
  ContentCardSubtitle,
  ContentCardTitle,
  Link,
  Typography,
  Utility,
} from '@visa/nova-react';

export const CategoryContentCard = () => {
  return (
    <ContentCard>
      <Utility element={<ContentCardBody />} vFlex vFlexCol vGap={4}>
        <Utility vAlignItems="center" vFlex vGap={6} vPaddingBottom={8}>
          <VisaAccountLow />
          <Typography style={{ color: 'var(--palette-default-active)' }} variant="overline" tag="h3">
            Category
          </Typography>
        </Utility>
        <ContentCardTitle variant="headline-4" tag="h4">
          Headline
        </ContentCardTitle>
        <ContentCardSubtitle variant="subtitle-3" tag="h5">
          Subtitle
        </ContentCardSubtitle>
        <Typography className="v-pt-4">
          This is optional text that describes the headline and subtitle in more detail.
        </Typography>
        <Utility vAlignItems="center" vFlex vGap={16} vPaddingTop={12}>
          <Button>Primary action</Button>
          <Link href="./content-card" noUnderline>
            Destination label <VisaChevronRightTiny rtl />
          </Link>
        </Utility>
      </Utility>
    </ContentCard>
  );
};

```

### Content card with icon
- **Section**: Default content cards
- **URL**: components/content-card/icon-content-card
- **Tags**: 
```tsx
import { VisaChevronRightTiny, VisaSecurityLockHigh } from '@visa/nova-icons-react';
import { ContentCard, ContentCardBody, ContentCardTitle, Divider, Link, Typography, Utility } from '@visa/nova-react';

export const IconContentCard = () => {
  return (
    <ContentCard>
      <Utility element={<ContentCardBody />} vFlex vFlexCol vGap={4}>
        <Utility element={<VisaSecurityLockHigh />} vPaddingBottom={12} />
        <ContentCardTitle variant="headline-4">Headline</ContentCardTitle>
        <Divider />
        <Typography className="v-pt-4">
          This is optional text that describes the headline and subtitle in more detail.
        </Typography>
        <Utility vPaddingTop={12}>
          <Link href="./content-card" noUnderline>
            Destination label <VisaChevronRightTiny rtl />
          </Link>
        </Utility>
      </Utility>
    </ContentCard>
  );
};

```

### Content card with image
- **Section**: Default content cards
- **URL**: components/content-card/image-header-content-card
- **Tags**: 
```tsx
import { VisaChevronRightTiny } from '@visa/nova-icons-react';
import {
  Button,
  ContentCard,
  ContentCardBody,
  ContentCardImage,
  ContentCardSubtitle,
  ContentCardTitle,
  Link,
  Typography,
  Utility,
} from '@visa/nova-react';

/// This is the base url for where your site is deployed. `import.meta.env.BASE_URL` is the environment variable used to import the base url for Vite. Change this import to match your build tool's base url.
const BASE_URL = import.meta.env.BASE_URL;

export const ImageHeaderContentCard = () => {
  return (
    <ContentCard style={{inlineSize: '50vw'}}>
      <ContentCardImage
        // If your image is NOT decorative, be sure to write alt text describing the image
        alt=""
        // Make sure the src path is correct for your image
        src={BASE_URL + '/content-card-image.png'}
        style={{ blockSize: 'auto', inlineSize: '100%', objectFit: 'contain', overflow: 'hidden' }}
        tag="img"
      />
      <Utility element={<ContentCardBody />} vFlex vFlexCol vGap={4}>
        <ContentCardTitle variant="headline-4">Headline</ContentCardTitle>
        <ContentCardSubtitle variant="subtitle-3">Subtitle</ContentCardSubtitle>
        <Typography className="v-pt-4">
          This is optional text that describes the headline and subtitle in more detail.
        </Typography>
        <Utility vAlignItems="center" vFlex vFlexWrap vGap={16} vPaddingTop={12}>
          <Button>Primary action</Button>
          <Link href="./content-card" noUnderline>
            Destination label <VisaChevronRightTiny rtl />
          </Link>
        </Utility>
      </Utility>
    </ContentCard>
  );
};

```

### Compact dashboard content card
- **Section**: Dashboard content cards
- **URL**: components/content-card/compact-dashboard-content-card
- **Tags**: 
```tsx
import { VisaArrowUpTiny } from '@visa/nova-icons-react';
import { ContentCard, ContentCardBody, ContentCardTitle, Typography, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'compact-dashboard-content-card';

export const CompactDashboardContentCard = () => {
  return (
    <ContentCard>
      <Utility element={<ContentCardBody />} vFlex vFlexCol vGap={4}>
        <Utility vAlignItems="center" vFlex vFlexRow vJustifyContent="between">
          <ContentCardTitle variant="headline-4">Headline</ContentCardTitle>
        </Utility>
        <Typography className="v-pt-4">
          This is optional text that describes the headline and subtitle in more detail.
        </Typography>
        <Utility vAlignItems="center" vFlex vFlexWrap vGap={16} vPaddingTop={12}>
          <Typography style={{ color: 'var(--palette-messaging-text-positive)' } as CSSProperties} variant="display-2">
            0,000
          </Typography>
          <Utility vAlignContent="end" vAlignItems="center" vFlex vFlexCol vGap={4} vMarginTop={8}>
            <VisaArrowUpTiny
              aria-hidden="false"
              title="Increasing value"
              titleId={`${id}-trend-title`}
              aria-labelledby={`${id}-trend-title ${id}-trend-label`}
            />
            <Typography id={`${id}-trend-label`} aria-hidden="true">
              Label
            </Typography>
          </Utility>
        </Utility>
      </Utility>
    </ContentCard>
  );
};

```

## Property Sections
### ContentCard
- **Selector**: <ContentCard />
- **Description**: Compact displays summarizing or directing users to more information.

### ContentCardBody
- **Selector**: <ContentCardBody />
- **Description**: Element containing the body elements of the content card.

### ContentCardImage
- **Selector**: <ContentCardImage />
- **Description**: Hero image for content card.

### ContentCardSubtitle
- **Selector**: <ContentCardSubtitle />
- **Description**: Subtitle component for content card. Extends typography component.

### ContentCardTitle
- **Selector**: <ContentCardTitle />
- **Description**: Title component for content card. Extends typography component.

## Properties
### borderBlockEnd
- **Section**: ContentCard
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Show bottom border on content card

### clickable
- **Section**: ContentCard
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Card Clickable

### ref
- **Section**: ContentCard
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: ContentCard
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: ContentCardBody
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: ContentCardBody
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: ContentCardImage
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: ContentCardImage
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### colorScheme
- **Section**: ContentCardSubtitle
- **Type**: "default" , "subtle" , "active" , "on-active"
- **Default**: 
- **Required**: false
- **Description**: Color variant

### ref
- **Section**: ContentCardSubtitle
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: ContentCardSubtitle
- **Type**: ElementType
- **Default**: h4
- **Required**: false
- **Description**: Tag of Component

### colorScheme
- **Section**: ContentCardTitle
- **Type**: "default" , "subtle" , "active" , "on-active"
- **Default**: 
- **Required**: false
- **Description**: Color variant

### ref
- **Section**: ContentCardTitle
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: ContentCardTitle
- **Type**: ElementType
- **Default**: h3
- **Required**: false
- **Description**: Tag of Component

