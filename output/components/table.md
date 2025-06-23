# table

## Metadata
- **Version**: 0.0.1
- **Description**: Grid that organizes information, enabling data interaction, manipulation, and criteria-based analysis using columns and rows.
- **Category**: components

## Example Sections
1. **Static tables with banded rows**
   - Description: 
2. **Static tables without banded rows**
   - Description: 
3. **Static tables with group headers**
   - Description: 
4. **Key value static tables**
   - Description: 

## Examples
### Large padding table with banded rows
- **Section**: Static tables with banded rows
- **URL**: components/table/large-padding-banded-table
- **Tags**: 
```tsx
import { ScreenReader, Table, Tbody, Td, Th, Thead, Tr } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const LargePaddingBandedTable = () => {
  return (
    <Table
      alternate
      style={
        {
          '--v-table-data-padding-block-default': 'var(--v-table-data-padding-block-large)',
          '--v-table-data-block-default': 'var(--v-table-data-block-large)',
        } as CSSProperties
      }
    >
      <ScreenReader tag="caption">Table with large padding and banded rows.</ScreenReader>
      <Thead>
        <Tr>
          <Th scope="col">Column A</Th>
          <Th scope="col">Column B</Th>
          <Th scope="col">Column C</Th>
          <Th scope="col">Column D</Th>
        </Tr>
      </Thead>
      <Tbody>
        <Tr>
          <Td>A1</Td>
          <Td>B1</Td>
          <Td>C1</Td>
          <Td>D1</Td>
        </Tr>
        <Tr>
          <Td>A2</Td>
          <Td>B2</Td>
          <Td>C2</Td>
          <Td>D2</Td>
        </Tr>
        <Tr>
          <Td>A3</Td>
          <Td>B3</Td>
          <Td>C3</Td>
          <Td>D3</Td>
        </Tr>
      </Tbody>
    </Table>
  );
};

```

### Medium padding table with banded rows
- **Section**: Static tables with banded rows
- **URL**: components/table/medium-padding-banded-table
- **Tags**: 
```tsx
import { ScreenReader, Table, Tbody, Td, Th, Thead, Tr } from '@visa/nova-react';

export const MediumPaddingBandedTable = () => {
  return (
    <Table alternate>
      <ScreenReader tag="caption">Table with medium padding and banded rows.</ScreenReader>
      <Thead>
        <Tr>
          <Th scope="col">Column A</Th>
          <Th scope="col">Column B</Th>
          <Th scope="col">Column C</Th>
          <Th scope="col">Column D</Th>
        </Tr>
      </Thead>
      <Tbody>
        <Tr>
          <Td>A1</Td>
          <Td>B1</Td>
          <Td>C1</Td>
          <Td>D1</Td>
        </Tr>
        <Tr>
          <Td>A2</Td>
          <Td>B2</Td>
          <Td>C2</Td>
          <Td>D2</Td>
        </Tr>
        <Tr>
          <Td>A3</Td>
          <Td>B3</Td>
          <Td>C3</Td>
          <Td>D3</Td>
        </Tr>
      </Tbody>
    </Table>
  );
};

```

### Small padding table with banded rows
- **Section**: Static tables with banded rows
- **URL**: components/table/small-padding-banded-table
- **Tags**: 
```tsx
import { CSSProperties } from 'react';
import { ScreenReader, Table, Tbody, Td, Th, Thead, Tr } from '@visa/nova-react';

export const SmallPaddingBandedTable = () => {
  return (
    <Table
      alternate
      style={
        {
          '--v-table-data-padding-block-default': 'var(--v-table-data-padding-block-small)',
          '--v-table-data-block-default': 'var(--v-table-data-block-small)',
        } as CSSProperties
      }
    >
      <ScreenReader tag="caption">Table with compact padding and banded rows.</ScreenReader>
      <Thead>
        <Tr>
          <Th scope="col">Column A</Th>
          <Th scope="col">Column B</Th>
          <Th scope="col">Column C</Th>
          <Th scope="col">Column D</Th>
        </Tr>
      </Thead>
      <Tbody>
        <Tr>
          <Td>A1</Td>
          <Td>B1</Td>
          <Td>C1</Td>
          <Td>D1</Td>
        </Tr>
        <Tr>
          <Td>A2</Td>
          <Td>B2</Td>
          <Td>C2</Td>
          <Td>D2</Td>
        </Tr>
        <Tr>
          <Td>A3</Td>
          <Td>B3</Td>
          <Td>C3</Td>
          <Td>D3</Td>
        </Tr>
      </Tbody>
    </Table>
  );
};

```

### Table with scrollbars and banded rows
- **Section**: Static tables with banded rows
- **URL**: components/table/scroll-table
- **Tags**: 
```tsx
import { CSSProperties } from 'react';
import { ScreenReader, Table, TableWrapper, Tbody, Td, Th, Thead, Tr } from '@visa/nova-react';

export const ScrollTable = () => {
  return (
    <TableWrapper
      style={{ '--v-table-wrapper-block-size': '288px', '--v-table-wrapper-inline-size': '576px' } as CSSProperties}
      tabIndex={0}
    >
      <Table alternate>
        <ScreenReader tag="caption">Table with extra data added to demo scrollable content.</ScreenReader>
        <Thead>
          <Tr>
            <Th scope="col">Column A</Th>
            <Th scope="col">Column B</Th>
            <Th scope="col">Column C</Th>
            <Th scope="col">Column D</Th>
            <Th scope="col">Column E</Th>
            <Th scope="col">Column F</Th>
            <Th scope="col">Column G</Th>
            <Th scope="col">Column H</Th>
            <Th scope="col">Column I</Th>
            <Th scope="col">Column J</Th>
            <Th scope="col">Column K</Th>
            <Th scope="col">Column L</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr>
            <Td>A1</Td>
            <Td>B1</Td>
            <Td>C1</Td>
            <Td>D1</Td>
            <Td>E1</Td>
            <Td>F1</Td>
            <Td>G1</Td>
            <Td>H1</Td>
            <Td>I1</Td>
            <Td>J1</Td>
            <Td>K1</Td>
            <Td>L1</Td>
          </Tr>
          <Tr>
            <Td>A2</Td>
            <Td>B2</Td>
            <Td>C2</Td>
            <Td>D2</Td>
            <Td>E2</Td>
            <Td>F2</Td>
            <Td>G2</Td>
            <Td>H2</Td>
            <Td>I2</Td>
            <Td>J2</Td>
            <Td>K2</Td>
            <Td>L2</Td>
          </Tr>
          <Tr>
            <Td>A3</Td>
            <Td>B3</Td>
            <Td>C3</Td>
            <Td>D3</Td>
            <Td>E3</Td>
            <Td>F3</Td>
            <Td>G3</Td>
            <Td>H3</Td>
            <Td>I3</Td>
            <Td>J3</Td>
            <Td>K3</Td>
            <Td>L3</Td>
          </Tr>
          <Tr>
            <Td>A4</Td>
            <Td>B4</Td>
            <Td>C4</Td>
            <Td>D4</Td>
            <Td>E4</Td>
            <Td>F4</Td>
            <Td>G4</Td>
            <Td>H4</Td>
            <Td>I4</Td>
            <Td>J4</Td>
            <Td>K4</Td>
            <Td>L4</Td>
          </Tr>
          <Tr>
            <Td>A5</Td>
            <Td>B5</Td>
            <Td>C5</Td>
            <Td>D5</Td>
            <Td>E5</Td>
            <Td>F5</Td>
            <Td>G5</Td>
            <Td>H5</Td>
            <Td>I5</Td>
            <Td>J5</Td>
            <Td>K5</Td>
            <Td>L5</Td>
          </Tr>
          <Tr>
            <Td>A6</Td>
            <Td>B6</Td>
            <Td>C6</Td>
            <Td>D6</Td>
            <Td>E6</Td>
            <Td>F6</Td>
            <Td>G6</Td>
            <Td>H6</Td>
            <Td>I6</Td>
            <Td>J6</Td>
            <Td>K6</Td>
            <Td>L6</Td>
          </Tr>
        </Tbody>
      </Table>
    </TableWrapper>
  );
};

```

### Table with lined rows
- **Section**: Static tables without banded rows
- **URL**: components/table/lined-rows-table
- **Tags**: 
```tsx
import { ScreenReader, Table, Tbody, Td, Th, Thead, Tr } from '@visa/nova-react';

export const LinedRowsTable = () => {
  return (
    <Table borderBlock>
      <ScreenReader tag="caption">Table with lined rows.</ScreenReader>
      <Thead>
        <Tr>
          <Th scope="col">Column A</Th>
          <Th scope="col">Column B</Th>
          <Th scope="col">Column C</Th>
          <Th scope="col">Column D</Th>
        </Tr>
      </Thead>
      <Tbody>
        <Tr>
          <Td>A1</Td>
          <Td>B1</Td>
          <Td>C1</Td>
          <Td>D1</Td>
        </Tr>
        <Tr>
          <Td>A2</Td>
          <Td>B2</Td>
          <Td>C2</Td>
          <Td>D2</Td>
        </Tr>
        <Tr>
          <Td>A3</Td>
          <Td>B3</Td>
          <Td>C3</Td>
          <Td>D3</Td>
        </Tr>
      </Tbody>
    </Table>
  );
};

```

### Table with outer border, column, and row dividers
- **Section**: Static tables without banded rows
- **URL**: components/table/outer-border-column-row-table
- **Tags**: 
```tsx
import { ScreenReader, Table, TableWrapper, Tbody, Td, Th, Thead, Tr } from '@visa/nova-react';

export const OuterBorderColumnRowDividerTable = () => {
  return (
    <TableWrapper>
      <Table border>
        <ScreenReader tag="caption">Table with outer borders on column and row dividers.</ScreenReader>
        <Thead>
          <Tr>
            <Th scope="col">Column A</Th>
            <Th scope="col">Column B</Th>
            <Th scope="col">Column C</Th>
            <Th scope="col">Column D</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr>
            <Td>A1</Td>
            <Td>B1</Td>
            <Td>C1</Td>
            <Td>D1</Td>
          </Tr>
          <Tr>
            <Td>A2</Td>
            <Td>B2</Td>
            <Td>C2</Td>
            <Td>D2</Td>
          </Tr>
          <Tr>
            <Td>A3</Td>
            <Td>B3</Td>
            <Td>C3</Td>
            <Td>D3</Td>
          </Tr>
        </Tbody>
      </Table>
    </TableWrapper>
  );
};

```

### Table with outer border and subtle headers
- **Section**: Static tables without banded rows
- **URL**: components/table/outer-border-subtle-header-table
- **Tags**: 
```tsx
import { ScreenReader, Table, TableWrapper, Tbody, Td, Th, Thead, Tr } from '@visa/nova-react';

export const OuterBorderSubtleHeaderTable = () => {
  return (
    <TableWrapper>
      <Table border subtle>
        <ScreenReader tag="caption">Table with outer borders and subtle headers.</ScreenReader>
        <Thead>
          <Tr>
            <Th scope="col">Column A</Th>
            <Th scope="col">Column B</Th>
            <Th scope="col">Column C</Th>
            <Th scope="col">Column D</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr>
            <Td>A1</Td>
            <Td>B1</Td>
            <Td>C1</Td>
            <Td>D1</Td>
          </Tr>
          <Tr>
            <Td>A2</Td>
            <Td>B2</Td>
            <Td>C2</Td>
            <Td>D2</Td>
          </Tr>
          <Tr>
            <Td>A3</Td>
            <Td>B3</Td>
            <Td>C3</Td>
            <Td>D3</Td>
          </Tr>
        </Tbody>
      </Table>
    </TableWrapper>
  );
};

```

### Table with group headers
- **Section**: Static tables with group headers
- **URL**: components/table/group-headers-table
- **Tags**: 
```tsx
import { ScreenReader, Table, Tbody, Td, Th, Thead, Tr } from '@visa/nova-react';

export const GroupHeadersTable = () => {
  return (
    <Table border>
      <ScreenReader tag="caption">Table with group headers.</ScreenReader>
      <Thead>
        <Tr className="v-typography-overline">
          <Th alternate colSpan={2}>
            Group header 1
          </Th>
          <Th alternate colSpan={2}>
            Group header 2
          </Th>
        </Tr>
        <Tr>
          <Th scope="col">Column A</Th>
          <Th scope="col">Column B</Th>
          <Th scope="col">Column C</Th>
          <Th scope="col">Column D</Th>
        </Tr>
      </Thead>
      <Tbody>
        <Tr>
          <Td>A1</Td>
          <Td>B1</Td>
          <Td>C1</Td>
          <Td>D1</Td>
        </Tr>
        <Tr>
          <Td>A2</Td>
          <Td>B2</Td>
          <Td>C2</Td>
          <Td>D2</Td>
        </Tr>
        <Tr>
          <Td>A3</Td>
          <Td>B3</Td>
          <Td>C3</Td>
          <Td>D3</Td>
        </Tr>
      </Tbody>
    </Table>
  );
};

```

### Table with group headers with empty cell
- **Section**: Static tables with group headers
- **URL**: components/table/group-headers-empty-cell-table
- **Tags**: 
```tsx
import { ScreenReader, Table, Tbody, Td, Th, Thead, Tr } from '@visa/nova-react';

export const GroupHeadersEmptyCellTable = () => {
  return (
    <Table border>
      <ScreenReader tag="caption">Table with group headers and an empty cell.</ScreenReader>
      <Thead>
        <Tr className="v-typography-overline">
          <Th alternate tag="td" />
          <Th alternate colSpan={1}>
            Group header 1
          </Th>
          <Th alternate colSpan={1}>
            Group header 2
          </Th>
        </Tr>
        <Tr>
          <Th scope="col">Column A</Th>
          <Th scope="col">Column B</Th>
          <Th scope="col">Column C</Th>
        </Tr>
      </Thead>
      <Tbody>
        <Tr>
          <Td>A1</Td>
          <Td>B1</Td>
          <Td>C1</Td>
        </Tr>
        <Tr>
          <Td>A2</Td>
          <Td>B2</Td>
          <Td>C2</Td>
        </Tr>
        <Tr>
          <Td>A3</Td>
          <Td>B3</Td>
          <Td>C3</Td>
        </Tr>
      </Tbody>
    </Table>
  );
};

```

### Key value table with banded rows
- **Section**: Key value static tables
- **URL**: components/table/key-value-banded-table
- **Tags**: 
```tsx
import { ScreenReader, Table, Tbody, Td, Tr } from '@visa/nova-react';

export const KeyValueBandedTable = () => {
  return (
    <Table alternate keyValue>
      <ScreenReader tag="caption">Table with banded key-value pairs.</ScreenReader>
      <Tbody>
        <Tr>
          <th className="v-td" scope="row">
            Key 1
          </th>
          <Td>Value 1</Td>
        </Tr>
        <Tr>
          <th className="v-td" scope="row">
            Key 2
          </th>
          <Td>Value 2</Td>
        </Tr>
        <Tr>
          <th className="v-td" scope="row">
            Key 3
          </th>
          <Td>Value 3</Td>
        </Tr>
        <Tr>
          <th className="v-td" scope="row">
            Key 4
          </th>
          <Td>Value 4</Td>
        </Tr>
      </Tbody>
    </Table>
  );
};

```

### Key value table with lined rows
- **Section**: Key value static tables
- **URL**: components/table/key-value-lined-table
- **Tags**: 
```tsx
import { ScreenReader, Table, TableWrapper, Tbody, Td, Tr } from '@visa/nova-react';

export const KeyValueLinedTable = () => {
  return (
    <TableWrapper>
      <Table keyValue border>
        <ScreenReader tag="caption">Table with lined key-value pairs.</ScreenReader>
        <Tbody>
          <Tr>
            <th className="v-td" scope="row">
              Key 1
            </th>
            <Td>Value 1</Td>
          </Tr>
          <Tr>
            <th className="v-td" scope="row">
              Key 2
            </th>
            <Td>Value 2</Td>
          </Tr>
          <Tr>
            <th className="v-td" scope="row">
              Key 3
            </th>
            <Td>Value 3</Td>
          </Tr>
          <Tr>
            <th className="v-td" scope="row">
              Key 4
            </th>
            <Td>Value 4</Td>
          </Tr>
        </Tbody>
      </Table>
    </TableWrapper>
  );
};

```

## Property Sections
### Table
- **Selector**: <Table />
- **Description**: Grid that organizes information, enabling data interaction, manipulation, and criteria-based analysis using columns and rows.

### TableWrapper
- **Selector**: <TableWrapper />
- **Description**: Container for a table that adds a border with a curved radius to the table.

### Tbody
- **Selector**: <Tbody />
- **Description**: Table body component that contains all the tr and td cells.

### Td
- **Selector**: <Td />
- **Description**: Table data cell component typically used for displaying data and content.

### Th
- **Selector**: <Th />
- **Description**: Table header cell component usually used for titles and column/row descriptions.

### Thead
- **Selector**: <Thead />
- **Description**: Table head component that contains all the th cells.

### Tr
- **Selector**: <Tr />
- **Description**: Table row component.

## Properties
### alternate
- **Section**: Table
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alt

### border
- **Section**: Table
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Borders all around the table and cells

### borderBlock
- **Section**: Table
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Borders only separating the rows

### keyValue
- **Section**: Table
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Key value pairs where text for the first column is bold.

### ref
- **Section**: Table
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### subtle
- **Section**: Table
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Subtle header

### ref
- **Section**: TableWrapper
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: TableWrapper
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: Tbody
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### ref
- **Section**: Td
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### alternate
- **Section**: Th
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alt

### ref
- **Section**: Th
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Th
- **Type**: ElementType
- **Default**: th
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: Thead
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### ref
- **Section**: Tr
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

