# breadcrumbs

## Metadata
- **Version**: 0.0.1
- **Description**: Supplemental navigation indicating the user's location in a site or app.
- **Category**: components

## Example Sections
1. **Examples**
   - Description: 

## Examples
### Breadcrumbs with default separator
- **Section**: Examples
- **URL**: components/breadcrumbs/default-breadcrumbs
- **Tags**: 
```tsx
import { Breadcrumbs, Link } from '@visa/nova-react';

export const DefaultBreadcrumbs = () => {
  return (
    <Breadcrumbs ariaLabel="Default breadcrumbs">
      <ol>
        <li>
          <Link href="./">L1 label</Link>
        </li>
        <li>
          <Link href="./">L2 label</Link>
        </li>
        <li>
          <Link href="./">L3 label</Link>
        </li>
        <li>
          <span aria-current="page">L4 label</span>
        </li>
      </ol>
    </Breadcrumbs>
  );
};

```

### Breadcrumbs with custom separator
- **Section**: Examples
- **URL**: components/breadcrumbs/custom-separator-breadcrumbs
- **Tags**: 
```tsx
import { Breadcrumbs, Link } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const CustomSeparatorBreadcrumbs = () => {
  return (
    <Breadcrumbs
      ariaLabel="Custom separator breadcrumbs"
      style={{ '--v-breadcrumbs-pseudo-separator': "'+'" } as CSSProperties}
    >
      <ol>
        <li>
          <Link href="./">L1 label</Link>
        </li>
        <li>
          <Link href="./">L2 label</Link>
        </li>
        <li>
          <Link href="./">L3 label</Link>
        </li>
        <li>
          <span aria-current="page">L4 label</span>
        </li>
      </ol>
    </Breadcrumbs>
  );
};

```

### Breadcrumbs with inline separator
- **Section**: Examples
- **URL**: components/breadcrumbs/inline-separator-breadcrumbs
- **Tags**: 
```tsx
import { Breadcrumbs, Link } from '@visa/nova-react';

export const InlineSeparatorBreadcrumbs = () => {
  return (
    <Breadcrumbs ariaLabel="Inline separator breadcrumbs" customSeparator>
      <ol>
        <li>
          <Link href="./">L1 label</Link> <span aria-hidden="true">|</span>
        </li>
        <li>
          <Link href="./">L2 label</Link> <span aria-hidden="true">|</span>
        </li>
        <li>
          <Link href="./">L3 label</Link> <span aria-hidden="true">|</span>
        </li>
        <li>
          <span aria-current="page">L4 label</span>
        </li>
      </ol>
    </Breadcrumbs>
  );
};

```

### Breadcrumbs with SVG separator
- **Section**: Examples
- **URL**: components/breadcrumbs/inline-svg-separator-breadcrumbs
- **Tags**: 
```tsx
import { VisaChevronRightTiny } from '@visa/nova-icons-react';
import { Breadcrumbs, Link } from '@visa/nova-react';

export const InlineSVGSeparatorBreadcrumbs = () => {
  return (
    <Breadcrumbs ariaLabel="Custom svg separator breadcrumbs" customSeparator>
      <ol>
        <li>
          <Link href="./">L1 label</Link> <VisaChevronRightTiny rtl />
        </li>
        <li>
          <Link href="./">L2 label</Link> <VisaChevronRightTiny rtl />
        </li>
        <li>
          <Link href="./">L3 label</Link> <VisaChevronRightTiny rtl />
        </li>
        <li>
          <span aria-current="page">L4 label</span>
        </li>
      </ol>
    </Breadcrumbs>
  );
};

```

## Property Sections
### Breadcrumbs
- **Selector**: <Breadcrumbs />
- **Description**: Supplemental navigation indicating the user's location in a site or app.

## Properties
### customSeparator
- **Section**: Breadcrumbs
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Use Custom Separator

### ref
- **Section**: Breadcrumbs
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Breadcrumbs
- **Type**: ElementType
- **Default**: nav
- **Required**: false
- **Description**: Tag of Component

