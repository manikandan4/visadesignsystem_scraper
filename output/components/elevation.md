# elevation

## Metadata
- **Version**: 0.0.1
- **Description**: 
- **Category**: utilities

## Example Sections
1. **Elevations**
   - Description: 

## Examples
### All elevations
- **Section**: Elevations
- **URL**: utilities/elevation/all-elevation
- **Tags**: 
```tsx
import { Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

// These styles simply makes a square box for demo purposes.
const defaultBoxStyle: CSSProperties = {
  alignItems: 'center',
  background: 'var(--palette-default-surface-2, #FFF)',
  display: 'flex',
  blockSize: 100,
  inlineSize: 100,
  justifyContent: 'center',
};

export const AllElevation = () => {
  return (
    <Utility vFlex vFlexWrap vGap={12}>
      <Utility vElevation="none" style={defaultBoxStyle}>
        None
      </Utility>
      <Utility vElevation="inset" style={defaultBoxStyle}>
        Inset
      </Utility>
      <Utility vElevation="xsmall" style={defaultBoxStyle}>
        XSmall
      </Utility>
      <Utility vElevation="small" style={defaultBoxStyle}>
        Small
      </Utility>
      <Utility vElevation="medium" style={defaultBoxStyle}>
        Medium
      </Utility>
      <Utility vElevation="large" style={defaultBoxStyle}>
        Large
      </Utility>
      <Utility vElevation="xlarge" style={defaultBoxStyle}>
        XLarge
      </Utility>
      <Utility vElevation="xxlarge" style={defaultBoxStyle}>
        XXLarge
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

