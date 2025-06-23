# divider

## Metadata
- **Version**: 0.0.1
- **Description**: Visual element used to separate and group information on a page.
- **Category**: components

## Example Sections
1. **Examples**
   - Description: 

## Examples
### Default divider
- **Section**: Examples
- **URL**: components/divider/default-divider
- **Tags**: 
```tsx
import { Divider } from '@visa/nova-react';

export const DefaultDivider = () => {
  return <Divider />;
};

```

### Section divider
- **Section**: Examples
- **URL**: components/divider/section-divider
- **Tags**: 
```tsx
import { Divider } from '@visa/nova-react';

export const SectionDivider = () => {
  return <Divider dividerType="section" />;
};

```

### Decorative divider
- **Section**: Examples
- **URL**: components/divider/decorative-divider
- **Tags**: 
```tsx
import { Divider } from '@visa/nova-react';

export const DecorativeDivider = () => {
  return <Divider dividerType="decorative" />;
};

```

## Property Sections
### Divider
- **Selector**: <Divider />
- **Description**: Visual element used to separate and group information on a page.

## Properties
### dividerType
- **Section**: Divider
- **Type**: "section" , "decorative"
- **Default**: 
- **Required**: false
- **Description**: Divider Type

### ref
- **Section**: Divider
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

