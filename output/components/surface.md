# surface

## Metadata
- **Version**: 0.0.1
- **Description**: Styles container to be used for alternate backgrounds.
- **Category**: components

## Example Sections
1. **Examples**
   - Description: 

## Examples
### Default
- **Section**: Examples
- **URL**: components/surface/default-surface
- **Tags**: 
```tsx
import { Surface } from '@visa/nova-react';

export const DefaultSurface = () => {
  return <Surface>Example</Surface>;
};

```

### Alternate
- **Section**: Examples
- **URL**: components/surface/alternate-surface
- **Tags**: 
```tsx
import { Surface } from '@visa/nova-react';

export const AlternateSurface = () => {
  return <Surface surfaceType="alternate">Example</Surface>;
};

```

## Property Sections
### Surface
- **Selector**: <Surface />
- **Description**: Styles container to be used for alternate backgrounds.

## Properties
### ref
- **Section**: Surface
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### surfaceType
- **Section**: Surface
- **Type**: "alternate"
- **Default**: 
- **Required**: false
- **Description**: Type of Surface

### tag
- **Section**: Surface
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

