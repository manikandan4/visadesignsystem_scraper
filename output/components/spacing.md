# spacing

## Metadata
- **Version**: 0.0.1
- **Description**: 
- **Category**: utilities

## Example Sections
1. **Gap**
   - Description: 
2. **Margin**
   - Description: 
3. **Padding**
   - Description: 

## Examples
### Default gap
- **Section**: Gap
- **URL**: utilities/spacing/gap-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const GapSpacing = () => {
  const itemCardStyles = { boxShadow: 'var(--elevation-medium)', inlineSize: 'auto' } as CSSProperties;
  return (
    <Utility vFlex>
      <Utility vFlex vColGap={20} style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
          Item 1
        </Utility>
        <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
          Item 2
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Column gap
- **Section**: Gap
- **URL**: utilities/spacing/gap-column-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const GapColumnSpacing = () => {
  const itemCardStyles = { boxShadow: 'var(--elevation-medium)', inlineSize: 'auto' } as CSSProperties;

  return (
    <Utility vFlex>
      <Utility vFlex vColGap={20} style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility vFlex vFlexCol>
          <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
            Item 1
          </Utility>
          <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
            Item 3
          </Utility>
        </Utility>
        <Utility vFlex vFlexCol>
          <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
            Item 2
          </Utility>
          <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
            Item 4
          </Utility>
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Row gap
- **Section**: Gap
- **URL**: utilities/spacing/gap-row-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const GapRowSpacing = () => {
  const itemCardStyles = { boxShadow: 'var(--elevation-medium)', inlineSize: 'auto' } as CSSProperties;

  return (
    <Utility vFlex>
      <Utility
        vFlex
        vFlexCol
        vRowGap={20}
        style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}
      >
        <Utility vFlex>
          <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
            Item 1
          </Utility>
          <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
            Item 2
          </Utility>
        </Utility>
        <Utility vFlex>
          <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
            Item 3
          </Utility>
          <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
            Item 4
          </Utility>
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Gap normal
- **Section**: Gap
- **URL**: utilities/spacing/gap-normal-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const GapNormalSpacing = () => {
  const itemCardStyles = { boxShadow: 'var(--elevation-medium)', inlineSize: 'auto' } as CSSProperties;
  return (
    <Utility vFlex>
      <Utility vFlex vGap="normal" style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
          Item 1
        </Utility>
        <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
          Item 2
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Gap inherit
- **Section**: Gap
- **URL**: utilities/spacing/gap-inherit-spacing
- **Tags**: 
```tsx
import { Avatar, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

const userCardStyles = {
  background: 'var(--palette-default-surface-1)',
  padding: 'var(--size-scalable-6) var(--size-scalable-80) var(--size-scalable-6) var(--size-scalable-20)',
} as CSSProperties;

const users = [
  {
    name: 'Alex Miller',
    initials: 'AM',
  },
  {
    name: 'Rosetta Jones',
    initials: 'RJ',
  },
  {
    name: 'Stacey Taylor',
    initials: 'ST',
  },
];

export const GapInheritSpacing = () => {
  return (
    <Utility vFlex>
      <Utility
        element={<ul />}
        vFlex
        vFlexCol
        vGap={8}
        style={
          {
            background: 'var(--palette-default-surface-highlight)',
          } as CSSProperties
        }
      >
        {users.map(u => (
          <Utility key={u.name} element={<li />} vFlex vAlignItems="center" vGap="inherit" style={userCardStyles}>
            <Avatar small aria-label={u.name}>
              {u.initials}
            </Avatar>
            {u.name}
          </Utility>
        ))}
      </Utility>
    </Utility>
  );
};

```

### Default margin
- **Section**: Margin
- **URL**: utilities/spacing/default-margin
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const DefaultMargin = () => {
  return (
    <Utility vFlex>
      <Utility vFlex style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility
          element={<Surface />}
          vMargin={20}
          style={{ border: '1px dashed var(--palette-default-active-subtle)' } as CSSProperties}
        >
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Margin top
- **Section**: Margin
- **URL**: utilities/spacing/margin-top-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const MarginTopSpacing = () => {
  return (
    <Utility vFlex>
      <Utility vFlex style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility
          element={<Surface />}
          vMarginTop={20}
          vPadding={16}
          style={{ border: '1px dashed var(--palette-default-active-subtle)' } as CSSProperties}
        >
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Margin bottom
- **Section**: Margin
- **URL**: utilities/spacing/margin-bottom-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const MarginBottomSpacing = () => {
  return (
    <Utility vFlex>
      <Utility vFlex style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility
          element={<Surface />}
          vMarginBottom={20}
          vPadding={16}
          style={{ border: '1px dashed var(--palette-default-active-subtle)' } as CSSProperties}
        >
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Margin left
- **Section**: Margin
- **URL**: utilities/spacing/margin-left-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const MarginLeftSpacing = () => {
  return (
    <Utility vFlex>
      <Utility vFlex style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility
          element={<Surface />}
          vMarginLeft={20}
          vPadding={16}
          style={{ border: '1px dashed var(--palette-default-active-subtle)' } as CSSProperties}
        >
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Margin right
- **Section**: Margin
- **URL**: utilities/spacing/margin-right-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const MarginRightSpacing = () => {
  return (
    <Utility vFlex>
      <Utility vFlex style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility
          element={<Surface />}
          vMarginRight={20}
          vPadding={16}
          style={{ border: '1px dashed var(--palette-default-active-subtle)' } as CSSProperties}
        >
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Margin horizontal
- **Section**: Margin
- **URL**: utilities/spacing/margin-horizontal-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const MarginHorizontalSpacing = () => {
  return (
    <Utility vFlex>
      <Utility vFlex style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility
          element={<Surface />}
          vMarginHorizontal={20}
          vPadding={16}
          style={{ border: '1px dashed var(--palette-default-active-subtle)' } as CSSProperties}
        >
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Margin vertical
- **Section**: Margin
- **URL**: utilities/spacing/margin-vertical-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const MarginVerticalSpacing = () => {
  return (
    <Utility vFlex>
      <Utility vFlex style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility
          element={<Surface />}
          vMarginVertical={20}
          vPadding={16}
          style={{ border: '1px dashed var(--palette-default-active-subtle)' } as CSSProperties}
        >
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Margin inherit
- **Section**: Margin
- **URL**: utilities/spacing/margin-inherit-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const MarginInheritSpacing = () => {
  return (
    <Utility vFlex>
      <Utility style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility
          vMarginTop={20}
          style={
            {
              textAlign: 'center',
              border: '1px dashed var(--palette-default-active-subtle)',
              background: 'var(--palette-messaging-highlight-positive)',
            } as CSSProperties
          }
        >
          <p>Parent with top margin</p>
          <Utility
            element={<Surface />}
            vMarginTop="inherit"
            vPadding={16}
            style={
              {
                border: '1px dashed var(--palette-default-active-subtle)',
                borderInline: 0,
                borderBlockEnd: 0,
              } as CSSProperties
            }
          >
            Child inherits top margin from parent
          </Utility>
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Padding
- **Section**: Padding
- **URL**: utilities/spacing/default-padding
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const DefaultPadding = () => {
  return (
    <Utility vFlex>
      <Utility
        vPadding={20}
        style={
          {
            background: 'var(--palette-default-surface-highlight)',
            border: '1px dashed var(--palette-default-active-subtle)',
          } as CSSProperties
        }
      >
        <Utility vPadding={16} element={<Surface />} vPaddingBottom={20}>
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Padding top
- **Section**: Padding
- **URL**: utilities/spacing/padding-top-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const PaddingTopSpacing = () => {
  return (
    <Utility vFlex>
      <Utility
        vPaddingTop={20}
        style={
          {
            background: 'var(--palette-default-surface-highlight)',
            border: '1px dashed var(--palette-default-active-subtle)',
          } as CSSProperties
        }
      >
        <Utility vPadding={16} element={<Surface />} vPaddingBottom={20}>
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};



```

### Padding bottom
- **Section**: Padding
- **URL**: utilities/spacing/padding-bottom-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const PaddingBottomSpacing = () => {
  return (
    <Utility vFlex>
      <Utility
        vPaddingBottom={20}
        style={
          {
            background: 'var(--palette-default-surface-highlight)',
            border: '1px dashed var(--palette-default-active-subtle)',
          } as CSSProperties
        }
      >
        <Utility vPadding={16} element={<Surface />} vPaddingBottom={20}>
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Padding left
- **Section**: Padding
- **URL**: utilities/spacing/padding-left-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const PaddingLeftSpacing = () => {
  return (
    <Utility vFlex>
      <Utility
        vPaddingLeft={20}
        style={
          {
            background: 'var(--palette-default-surface-highlight)',
            border: '1px dashed var(--palette-default-active-subtle)',
          } as CSSProperties
        }
      >
        <Utility vPadding={16} element={<Surface />} vPaddingBottom={20}>
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Padding right
- **Section**: Padding
- **URL**: utilities/spacing/padding-right-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const PaddingRightSpacing = () => {
  return (
    <Utility vFlex>
      <Utility
        vPaddingRight={20}
        style={
          {
            background: 'var(--palette-default-surface-highlight)',
            border: '1px dashed var(--palette-default-active-subtle)',
          } as CSSProperties
        }
      >
        <Utility vPadding={16} element={<Surface />} vPaddingBottom={20}>
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};


```

### Padding horizontal
- **Section**: Padding
- **URL**: utilities/spacing/padding-horizontal-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const PaddingHorizontalSpacing = () => {
  return (
    <Utility vFlex>
      <Utility
        vPaddingHorizontal={20}
        style={
          {
            background: 'var(--palette-default-surface-highlight)',
            border: '1px dashed var(--palette-default-active-subtle)',
          } as CSSProperties
        }
      >
        <Utility vPadding={16} element={<Surface />} vPaddingBottom={20}>
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Padding vertical
- **Section**: Padding
- **URL**: utilities/spacing/padding-vertical-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const PaddingVerticalSpacing = () => {
  return (
    <Utility vFlex>
      <Utility
        vPaddingVertical={20}
        style={
          {
            background: 'var(--palette-default-surface-highlight)',
            border: '1px dashed var(--palette-default-active-subtle)',
          } as CSSProperties
        }
      >
        <Utility vPadding={16} element={<Surface />} vPaddingBottom={20}>
          Content Area
        </Utility>
      </Utility>
    </Utility>
  );
};

```

### Padding inherit
- **Section**: Padding
- **URL**: utilities/spacing/padding-inherit-spacing
- **Tags**: 
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const PaddingInheritSpacing = () => {
  return (
    <Utility vFlex>
      <Utility
        vPaddingTop={24}
        style={
          {
            textAlign: 'center',
            border: '1px dashed var(--palette-default-active-subtle)',
            background: 'var(--palette-default-surface-highlight)',
          } as CSSProperties
        }
      >
        <p>Parent with top padding</p>
        <Utility
          element={<Surface />}
          vPaddingTop="inherit"
          vPadding={16}
          style={
            {
              border: '1px dashed var(--palette-default-active-subtle)',
              borderInline: 0,
              borderBlockEnd: 0,
            } as CSSProperties
          }
        >
          Child inherits top margin from parent
        </Utility>
      </Utility>
    </Utility>
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

