# link

## Metadata
- **Version**: 0.0.1
- **Description**: Text-based navigation elements that directs users to another destination.
- **Category**: components

## Example Sections
1. **Standalone links**
   - Description: 
2. **Inline links**
   - Description: 
3. **Links coded as buttons**
   - Description: 
4. **Custom examples**
   - Description: 

## Examples
### Default link
- **Section**: Standalone links
- **URL**: components/link/default-link
- **Tags**: docs
```tsx
import { Link } from '@visa/nova-react';

export const DefaultLink = () => {
  return <Link href="./link">Destination label</Link>;
};

```

### Link with leading icon
- **Section**: Standalone links
- **URL**: components/link/leading-icon-link
- **Tags**: docs
```tsx
import { VisaArrowBackTiny } from '@visa/nova-icons-react';
import { Link } from '@visa/nova-react';

export const LeadingIconLink = () => {
  return (
    <Link href="./link" noUnderline>
      <VisaArrowBackTiny />
      Destination label
    </Link>
  );
};

```

### Link with trailing icon
- **Section**: Standalone links
- **URL**: components/link/trailing-icon-link
- **Tags**: docs
```tsx
import { VisaChevronRightTiny } from '@visa/nova-icons-react';
import { Link } from '@visa/nova-react';

export const TrailingIconLink = () => {
  return (
    <Link href="./link" noUnderline>
      Destination label
      <VisaChevronRightTiny />
    </Link>
  );
};

```

### Alternate link with trailing icon
- **Section**: Standalone links
- **URL**: components/link/alternate-link
- **Tags**: alternate, docs
```tsx
import { VisaChevronRightTiny } from '@visa/nova-icons-react';
import { Link } from '@visa/nova-react';

export const AlternateLink = () => {
  return (
    <Link alternate href="./link" noUnderline>
      Destination label
      <VisaChevronRightTiny />
    </Link>
  );
};

```

### Link that opens in a new tab
- **Section**: Standalone links
- **URL**: components/link/new-tab-link
- **Tags**: 
```tsx
import { VisaMaximizeTiny } from '@visa/nova-icons-react';
import { Link } from '@visa/nova-react';

export const NewTabLink = () => {
  return (
    <Link
      aria-label="Destination label (opens in a new tab)"
      href="./link"
      noUnderline
      target="_blank"
      rel="noopener noreferrer"
    >
      Destination label
      <VisaMaximizeTiny />
    </Link>
  );
};

```

### Disabled link
- **Section**: Standalone links
- **URL**: components/link/disabled-link
- **Tags**: docs
```tsx
import { Link } from '@visa/nova-react';

export const DisabledLink = () => {
  return (
    <Link disabled role="link">
      Destination label
    </Link>
  );
};

```

### Inline link
- **Section**: Inline links
- **URL**: components/link/inline-link
- **Tags**: docs
```tsx
import { Link, Typography } from '@visa/nova-react';

export const InlineLink = () => {
  return (
    <Typography>
      This is a sentence with an inline <Link href="./link">destination label</Link>.
    </Typography>
  );
};

```

### Inline link with trailing icon
- **Section**: Inline links
- **URL**: components/link/without-underline-link
- **Tags**: 
```tsx
import { VisaMaximizeTiny } from '@visa/nova-icons-react';
import { Link, Typography } from '@visa/nova-react';

export const WithoutUnderlineLink = () => {
  return (
    <Typography>
      This is a sentence with an inline{' '}
      <Link aria-label="destination label (opens in a new tab)" href="./link" noUnderline>
        destination label
        <VisaMaximizeTiny />
      </Link>
    </Typography>
  );
};

```

### Link coded as a button
- **Section**: Links coded as buttons
- **URL**: components/link/custom-tag-link
- **Tags**: docs
```tsx
import { VisaDevicePrinterTiny } from '@visa/nova-icons-react';
import { Link } from '@visa/nova-react';

export const CustomTagLink = () => {
  return (
    <Link noUnderline element={<button />}>
      Print
      <VisaDevicePrinterTiny />
    </Link>
  );
};

```

### Disabled link coded as a button
- **Section**: Links coded as buttons
- **URL**: components/link/disabled-custom-tag-link
- **Tags**: 
```tsx
import { VisaDevicePrinterTiny } from '@visa/nova-icons-react';
import { Link } from '@visa/nova-react';

export const DisabledCustomTagLink = () => {
  return (
    <Link noUnderline element={<button disabled/>}>
      Print
      <VisaDevicePrinterTiny />
    </Link>
  );
};

```

### Link uses React Router DOM
- **Section**: Custom examples
- **URL**: components/link/react-router-link
- **Tags**: custom
```tsx
import { Link } from 'react-router-dom';
import { Link as VLink } from '@visa/nova-react';

export const ReactRouterLink = () => {
  return (
    <>
      This <VLink element={<Link to={'./'}>link</Link>} /> goes to this current page.
    </>
  );
};

```

### Link with custom typography
- **Section**: Custom examples
- **URL**: components/link/custom-typography-link
- **Tags**: custom
```tsx
import { VisaChevronRightTiny } from '@visa/nova-icons-react';
import { Link, Typography } from '@visa/nova-react';

export const CustomTypographyLink = () => {
  return (
    <Link href="./link" noUnderline>
      <Typography variant="headline-3">
        Destination label (headline 3) <VisaChevronRightTiny /> 
      </Typography>
    </Link>
  );
};

```

## Property Sections
### Link
- **Selector**: <Link />
- **Description**: Text-based navigation elements that directs users to another destination.

## Properties
### alternate
- **Section**: Link
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate color scheme

### element
- **Section**: Link
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### noUnderline
- **Section**: Link
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: No Underline

### ref
- **Section**: Link
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### skipLink
- **Section**: Link
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Skip Link

### tag
- **Section**: Link
- **Type**: ElementType
- **Default**: a
- **Required**: false
- **Description**: Tag (not compatible with element property)

