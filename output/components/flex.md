# flex

## Metadata
- **Version**: 0.0.1
- **Description**: 
- **Category**: utilities

## Example Sections
1. **Flex displays**
   - Description: 
2. **Flex column**
   - Description: 
3. **Flex row**
   - Description: 
4. **Flex wrap**
   - Description: 
5. **Flex grow**
   - Description: 
6. **Flex shrink**
   - Description: 
7. **Flex align**
   - Description: 
8. **Flex justify**
   - Description: 

## Examples
### Flex default
- **Section**: Flex displays
- **URL**: utilities/flex/default-flex
- **Tags**: 
```tsx
import { Utility } from '@visa/nova-react';

export const DefaultFlex = () => {
  return (
    <Utility vFlex vGap={4}>
      This is a flex container
    </Utility>
  );
};

```

### Inline flex
- **Section**: Flex displays
- **URL**: utilities/flex/inline-flex
- **Tags**: 
```tsx
import { Utility } from '@visa/nova-react';

export const InlineFlex = () => {
  return (
    <Utility vFlexInline vGap={4}>
      This is an inline flex container
    </Utility>
  );
};

```

### Flex column
- **Section**: Flex column
- **URL**: utilities/flex/column-flex
- **Tags**: 
```tsx
import { Utility } from '@visa/nova-react';

export const ColumnFlex = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <span>first</span>
      <span>second</span>
      <span>third</span>
    </Utility>
  );
};

```

### Flex column reverse
- **Section**: Flex column
- **URL**: utilities/flex/column-reverse-flex
- **Tags**: 
```tsx
import { Utility } from '@visa/nova-react';

export const ColumnReverseFlex = () => {
  return (
    <Utility vFlex vFlexColReverse vGap={4}>
      <span>first</span>
      <span>second</span>
      <span>third</span>
    </Utility>
  );
};

```

### Flex row
- **Section**: Flex row
- **URL**: utilities/flex/row-flex
- **Tags**: 
```tsx
import { Utility } from '@visa/nova-react';

export const RowFlex = () => {
  return (
    <Utility vFlex vFlexRow vGap={4}>
      <span>first</span>
      <span>second</span>
      <span>third</span>
    </Utility>
  );
};

```

### Flex row reverse
- **Section**: Flex row
- **URL**: utilities/flex/row-reverse-flex
- **Tags**: 
```tsx
import { Utility } from '@visa/nova-react';

export const RowReverseFlex = () => {
  return (
    <Utility vFlex vFlexRowReverse vGap={4}>
      <span>first</span>
      <span>second</span>
      <span>third</span>
    </Utility>
  );
};

```

### Flex wrap
- **Section**: Flex wrap
- **URL**: utilities/flex/wrap-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const WrapFlex = () => {
  return (
    <UtilityFragment vFlex vFlexWrap vGap={4}>
      <Surface style={{ '--v-surface-border-size': '2px', '--v-surface-inline-size': '150px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
        <span>fifth</span>
        <span>sixth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex wrap reverse
- **Section**: Flex wrap
- **URL**: utilities/flex/wrap-reverse-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const WrapReverseFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexWrapReverse vGap={4}>
      <Surface style={{ '--v-surface-border-size': '2px', '--v-surface-inline-size': '150px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
        <span>fifth</span>
        <span>sixth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex no wrap
- **Section**: Flex wrap
- **URL**: utilities/flex/no-wrap-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const NoWrapFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexNoWrap vGap={4}>
      <Surface style={{ '--v-surface-border-size': '2px', '--v-surface-inline-size': '150px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
        <span>fifth</span>
        <span>sixth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex grow
- **Section**: Flex grow
- **URL**: utilities/flex/grow-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, Utility, UtilityFragment } from '@visa/nova-react';

export const GrowFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ '--v-surface-border-size': '2px' } as CSSProperties}>
        <Utility tag="span" vFlexGrow>
          first
        </Utility>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex grow 0
- **Section**: Flex grow
- **URL**: utilities/flex/grow-zero-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, Utility, UtilityFragment } from '@visa/nova-react';

export const GrowZeroFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ '--v-surface-border-size': '2px' } as CSSProperties}>
        <Utility tag="span" vFlexGrow0>
          first
        </Utility>
        <Utility tag="span" vFlexGrow>
          second
        </Utility>
        <Utility tag="span" vFlexGrow>
          third
        </Utility>
        <Utility tag="span" vFlexGrow>
          fourth
        </Utility>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex shrink
- **Section**: Flex shrink
- **URL**: utilities/flex/shrink-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, Utility, UtilityFragment } from '@visa/nova-react';

export const ShrinkFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ '--v-surface-border-size': '2px' } as CSSProperties}>
        <Utility tag="span" vFlexShrink>
          first
        </Utility>
        <Utility tag="span" vFlexGrow>
          second
        </Utility>
        <Utility tag="span" vFlexGrow>
          third
        </Utility>
        <Utility tag="span" vFlexGrow>
          fourth
        </Utility>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex shrink 0
- **Section**: Flex shrink
- **URL**: utilities/flex/shrink-zero-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, Utility, UtilityFragment } from '@visa/nova-react';

export const ShrinkZeroFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vGap={4} vFlexWrap>
      <Surface style={{ '--v-surface-border-size': '2px' } as CSSProperties}>
        <Utility tag="span" vFlexShrink0>
          first
        </Utility>
        <Utility tag="span" vFlexShrink>
          second
        </Utility>
        <Utility tag="span" vFlexShrink>
          third
        </Utility>
        <Utility tag="span" vFlexShrink>
          fourth
        </Utility>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align content center
- **Section**: Flex align
- **URL**: utilities/flex/align-content-center-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignContentCenterFlex = () => {
  return (
    <UtilityFragment vAlignContent="center" vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align content start
- **Section**: Flex align
- **URL**: utilities/flex/align-content-start-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignContentStartFlex = () => {
  return (
    <UtilityFragment vAlignContent="start" vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align content end
- **Section**: Flex align
- **URL**: utilities/flex/align-content-end-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignContentEndFlex = () => {
  return (
    <UtilityFragment vAlignContent="end" vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align content space between
- **Section**: Flex align
- **URL**: utilities/flex/align-content-between-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignContentBetweenFlex = () => {
  return (
    <UtilityFragment vAlignContent="between" vFlex vFlexRow vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align content around
- **Section**: Flex align
- **URL**: utilities/flex/align-content-around-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignContentAroundFlex = () => {
  return (
    <UtilityFragment vAlignContent="around" vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align content evenly
- **Section**: Flex align
- **URL**: utilities/flex/align-content-evenly-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignContentEvenlyFlex = () => {
  return (
    <UtilityFragment vAlignContent="evenly" vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align items start
- **Section**: Flex align
- **URL**: utilities/flex/align-items-start-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignItemsStartFlex = () => {
  return (
    <UtilityFragment vAlignItems="start" vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align items end
- **Section**: Flex align
- **URL**: utilities/flex/align-items-end-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignItemsEndFlex = () => {
  return (
    <UtilityFragment vAlignItems="end" vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align items center
- **Section**: Flex align
- **URL**: utilities/flex/align-items-center-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignItemsCenterFlex = () => {
  return (
    <UtilityFragment vAlignItems="center" vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align items baseline
- **Section**: Flex align
- **URL**: utilities/flex/align-items-baseline-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignItemsBaselineFlex = () => {
  return (
    <UtilityFragment vAlignItems="baseline" vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align items stretch
- **Section**: Flex align
- **URL**: utilities/flex/align-items-stretch-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignItemsStretchFlex = () => {
  return (
    <UtilityFragment vAlignItems="stretch" vFlex vFlexRow vFlexWrap vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align self start
- **Section**: Flex align
- **URL**: utilities/flex/align-self-start-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignSelfStartFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <UtilityFragment vFlex vAlignSelf="start">
          <Surface surfaceType="alternate">self</Surface>
        </UtilityFragment>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align self end
- **Section**: Flex align
- **URL**: utilities/flex/align-self-end-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignSelfEndFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <UtilityFragment vFlex vAlignSelf="end">
          <Surface surfaceType="alternate">self</Surface>
        </UtilityFragment>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align self auto
- **Section**: Flex align
- **URL**: utilities/flex/align-self-auto-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignSelfAutoFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <UtilityFragment vAlignSelf="auto" vFlex>
          <Surface surfaceType="alternate">self</Surface>
        </UtilityFragment>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align self center
- **Section**: Flex align
- **URL**: utilities/flex/align-self-center-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignSelfCenterFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <UtilityFragment vAlignSelf="center" vFlex>
          <Surface surfaceType="alternate">self</Surface>
        </UtilityFragment>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex align self stretch
- **Section**: Flex align
- **URL**: utilities/flex/align-self-stretch-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const AlignSelfStretchFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vGap={4}>
      <Surface style={{ blockSize: '80px', '--v-surface-border-size': '2px' } as CSSProperties}>
        <UtilityFragment vFlex vAlignSelf="stretch">
          <Surface surfaceType="alternate">self</Surface>
        </UtilityFragment>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex justify content start
- **Section**: Flex justify
- **URL**: utilities/flex/justify-content-start-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const JustifyContentStartFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexWrap vGap={4} vJustifyContent="start">
      <Surface style={{ '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex justify content end
- **Section**: Flex justify
- **URL**: utilities/flex/justify-content-end-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const JustifyContentEndFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexWrap vGap={4} vJustifyContent="end">
      <Surface style={{ '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex justify content center
- **Section**: Flex justify
- **URL**: utilities/flex/justify-content-center-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const JustifyContentCenterFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexWrap vGap={4} vJustifyContent="center">
      <Surface style={{ '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex justify content space between
- **Section**: Flex justify
- **URL**: utilities/flex/justify-content-between-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const JustifyContentBetweenFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexWrap vJustifyContent="between" vGap={4}>
      <Surface style={{ '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex justify content around
- **Section**: Flex justify
- **URL**: utilities/flex/justify-content-around-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const JustifyContentAroundFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexWrap vGap={4} vJustifyContent="around">
      <Surface style={{ '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

### Flex justify content evenly
- **Section**: Flex justify
- **URL**: utilities/flex/justify-content-evenly-flex
- **Tags**: 
```tsx
import { CSSProperties } from 'react';

import { Surface, UtilityFragment } from '@visa/nova-react';

export const JustifyContentEvenlyFlex = () => {
  return (
    <UtilityFragment vFlex vFlexRow vFlexWrap vGap={4} vJustifyContent="evenly">
      <Surface style={{ '--v-surface-border-size': '2px' } as CSSProperties}>
        <span>first</span>
        <span>second</span>
        <span>third</span>
        <span>fourth</span>
      </Surface>
    </UtilityFragment>
  );
};

```

## Property Sections
### Utility
- **Selector**: <Utility />
- **Description**: Component used to create a div, by default, with the correct Nova utility style classes applied.

### UtilityFragment
- **Selector**: <UtilityFragment />
- **Description**: Wraps around a component and add Nova utility classes to its direct child without adding extra elements to the DOM.

## Properties
### element
- **Section**: Utility
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### ref
- **Section**: Utility
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Utility
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag (not compatible with element property)

### vAlignContent
- **Section**: Utility
- **Type**: "center" , "start" , "end" , "around" , "between" , "evenly"
- **Default**: 
- **Required**: false
- **Description**: 

### vAlignItems
- **Section**: Utility
- **Type**: "center" , "start" , "baseline" , "end" , "stretch"
- **Default**: 
- **Required**: false
- **Description**: 

### vAlignSelf
- **Section**: Utility
- **Type**: "center" , "start" , "auto" , "end" , "stretch"
- **Default**: 
- **Required**: false
- **Description**: 

### vColGap
- **Section**: Utility
- **Type**: 0 , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vContainerHide
- **Section**: Utility
- **Type**: "xs" , "sm" , "md" , "lg" , "xl" , "xxl" , "desktop" , "mobile"
- **Default**: 
- **Required**: false
- **Description**: 

### vElevation
- **Section**: Utility
- **Type**: "small" , "none" , "large" , "inset" , "medium" , "xlarge" , "xxlarge" , "xsmall"
- **Default**: 
- **Required**: false
- **Description**: 

### vFlex
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexCol
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexColReverse
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexGrow
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexGrow0
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexInline
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexNoWrap
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexRow
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexRowReverse
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexShrink
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexShrink0
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexWrap
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexWrapReverse
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vGap
- **Section**: Utility
- **Type**: Omit
- **Default**: 
- **Required**: false
- **Description**: 

### vHide
- **Section**: Utility
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vJustifyContent
- **Section**: Utility
- **Type**: "center" , "start" , "end" , "around" , "between" , "evenly"
- **Default**: 
- **Required**: false
- **Description**: 

### vMargin
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginBottom
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginHorizontal
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginLeft
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginRight
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginTop
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginVertical
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMediaHide
- **Section**: Utility
- **Type**: "xs" , "sm" , "md" , "lg" , "xl" , "xxl" , "desktop" , "mobile"
- **Default**: 
- **Required**: false
- **Description**: 

### vPadding
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingBottom
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingHorizontal
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingLeft
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingRight
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingTop
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingVertical
- **Section**: Utility
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vRowGap
- **Section**: Utility
- **Type**: 0 , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### children
- **Section**: UtilityFragment
- **Type**: ReactElement
- **Default**: 
- **Required**: true
- **Description**: Child element that the styles are applies to. Only allows for single child element.

### vAlignContent
- **Section**: UtilityFragment
- **Type**: "center" , "start" , "end" , "around" , "between" , "evenly"
- **Default**: 
- **Required**: false
- **Description**: 

### vAlignItems
- **Section**: UtilityFragment
- **Type**: "center" , "start" , "baseline" , "end" , "stretch"
- **Default**: 
- **Required**: false
- **Description**: 

### vAlignSelf
- **Section**: UtilityFragment
- **Type**: "center" , "start" , "auto" , "end" , "stretch"
- **Default**: 
- **Required**: false
- **Description**: 

### vColGap
- **Section**: UtilityFragment
- **Type**: 0 , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vContainerHide
- **Section**: UtilityFragment
- **Type**: "xs" , "sm" , "md" , "lg" , "xl" , "xxl" , "desktop" , "mobile"
- **Default**: 
- **Required**: false
- **Description**: 

### vElevation
- **Section**: UtilityFragment
- **Type**: "small" , "none" , "large" , "inset" , "medium" , "xlarge" , "xxlarge" , "xsmall"
- **Default**: 
- **Required**: false
- **Description**: 

### vFlex
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexCol
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexColReverse
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexGrow
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexGrow0
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexInline
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexNoWrap
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexRow
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexRowReverse
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexShrink
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexShrink0
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexWrap
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vFlexWrapReverse
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vGap
- **Section**: UtilityFragment
- **Type**: Omit
- **Default**: 
- **Required**: false
- **Description**: 

### vHide
- **Section**: UtilityFragment
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: 

### vJustifyContent
- **Section**: UtilityFragment
- **Type**: "center" , "start" , "end" , "around" , "between" , "evenly"
- **Default**: 
- **Required**: false
- **Description**: 

### vMargin
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginBottom
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginHorizontal
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginLeft
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginRight
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginTop
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMarginVertical
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vMediaHide
- **Section**: UtilityFragment
- **Type**: "xs" , "sm" , "md" , "lg" , "xl" , "xxl" , "desktop" , "mobile"
- **Default**: 
- **Required**: false
- **Description**: 

### vPadding
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingBottom
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingHorizontal
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingLeft
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingRight
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingTop
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vPaddingVertical
- **Section**: UtilityFragment
- **Type**: 0 , "inherit" , "auto" , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

### vRowGap
- **Section**: UtilityFragment
- **Type**: 0 , 1 , 48 , 4 , 10 , 3 , 2 , 5 , 6 , 7 , 8 , 9 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47
- **Default**: 
- **Required**: false
- **Description**: 

