# icon

## Metadata
- **Version**: 0.0.1
- **Description**: Meant for use with sprites only. Uses dom href linking of sprite elements expected to already be in the DOM to render the icon.
- **Category**: components

## Example Sections
1. **Icon styles**
   - Description: 
2. **Icon sizes**
   - Description: 
3. **Icon customizations**
   - Description: 

## Examples
### Default
- **Section**: Icon styles
- **URL**: components/icon/default-icon
- **Tags**: 
```tsx
import { VisaGlobalLow } from '@visa/nova-icons-react';

export const DefaultIcon = () => {
  return <VisaGlobalLow aria-hidden="false" aria-label="global" />;
};

```

### Visa
- **Section**: Icon styles
- **URL**: components/icon/visa-icon
- **Tags**: 
```tsx
import { VisaInformationLow } from '@visa/nova-icons-react';

export const VisaIcon = () => {
  return <VisaInformationLow aria-hidden="false" aria-label="info" />;
};

```

### Generic
- **Section**: Icon styles
- **URL**: components/icon/generic-icon
- **Tags**: 
```tsx
import { GenericInformationLow } from '@visa/nova-icons-react';

export const GenericIcon = () => {
  return <GenericInformationLow aria-hidden="false" aria-label="info" />;
};

```

### Tiny resolution
- **Section**: Icon sizes
- **URL**: components/icon/tiny-resolution
- **Tags**: 
```tsx
import { VisaInformationTiny } from '@visa/nova-icons-react';

export const TinyResolution = () => {
  return <VisaInformationTiny aria-hidden="false" aria-label="info" />;
};

```

### Low resolution
- **Section**: Icon sizes
- **URL**: components/icon/low-resolution
- **Tags**: 
```tsx
import { VisaInformationLow } from '@visa/nova-icons-react';

export const LowResolution = () => {
  return <VisaInformationLow aria-hidden="false" aria-label="info" />;
};

```

### High resolution
- **Section**: Icon sizes
- **URL**: components/icon/high-resolution
- **Tags**: 
```tsx
import { VisaInformationHigh } from '@visa/nova-icons-react';

export const HighResolution = () => {
  return <VisaInformationHigh aria-hidden="false" aria-label="info" />;
};

```

### Icon with right-to-left support
- **Section**: Icon customizations
- **URL**: components/icon/rtl-icon
- **Tags**: custom
```tsx
import { VisaChevronRightLow } from '@visa/nova-icons-react';

export const RtlIcons = () => {
  return <VisaChevronRightLow rtl />;
};

```

### Icon with custom colors
- **Section**: Icon customizations
- **URL**: components/icon/custom-color-icon
- **Tags**: 
```tsx
import { VisaHomeHigh } from '@visa/nova-icons-react';
import { CSSProperties } from 'react';

export const CustomColorIcon = () => {
  return <VisaHomeHigh style={{ '--v-icon-primary': 'teal', '--v-icon-secondary': 'orange' } as CSSProperties} />;
};

```

## Property Sections
### Icon
- **Selector**: <Icon />
- **Description**: Meant for use with sprites only. Uses dom href linking of sprite elements expected to already be in the DOM to render the icon.

## Properties
### ariaBaseId
- **Section**: Icon
- **Type**: string , number
- **Default**: 
- **Required**: false
- **Description**: Aria Base ID

### brand
- **Section**: Icon
- **Type**: "generic" , "visa"
- **Default**: generic
- **Required**: false
- **Description**: Icon Branding

### description
- **Section**: Icon
- **Type**: string
- **Default**: 
- **Required**: false
- **Description**: 

### iconName
- **Section**: Icon
- **Type**: string
- **Default**: help
- **Required**: false
- **Description**: Name of Icon

### resolution
- **Section**: Icon
- **Type**: "high" , "low" , "tiny"
- **Default**: low
- **Required**: false
- **Description**: Resolution of Icon

### rtl
- **Section**: Icon
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Flips icon horizontally when document direction is set to right to left

### title
- **Section**: Icon
- **Type**: string
- **Default**: 
- **Required**: false
- **Description**: Title for Standalone SVG's

