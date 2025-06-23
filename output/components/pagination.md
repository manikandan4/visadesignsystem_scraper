# pagination

## Metadata
- **Version**: 0.0.1
- **Description**: Set of links used to navigate content split across multiple pages.
- **Category**: components

## Example Sections
1. **Default paginations**
   - Description: 
2. **Slim paginations**
   - Description: 
3. **Custom paginations**
   - Description: 

## Examples
### Default pagination with first page selected
- **Section**: Default paginations
- **URL**: components/pagination/one-digit-pagination
- **Tags**: 
```tsx
import {
  VisaArrowEndTiny,
  VisaArrowStartTiny,
  VisaChevronLeftTiny,
  VisaChevronRightTiny,
  VisaOptionHorizontalTiny,
} from '@visa/nova-icons-react';
import { Button, Pagination, PaginationOverflow } from '@visa/nova-react';

export const OneDigitPagination = () => {
  return (
    <nav aria-label="1 digit pagination" role="navigation">
      <Pagination className="v-flex v-flex-row v-align-items-center v-gap-4">
        <li className="v-mobile-container-hide">
          <Button aria-label="Go to first page" buttonSize="small" colorScheme="tertiary" disabled iconButton>
            <VisaArrowStartTiny rtl />
          </Button>
        </li>
        <li>
          <Button aria-label="Go to previous page" buttonSize="small" colorScheme="tertiary" disabled iconButton>
            <VisaChevronLeftTiny rtl />
          </Button>
        </li>
        <li>
          <Button aria-current="true" aria-label="Page 1" colorScheme="tertiary">
            1
          </Button>
        </li>
        <li>
          <Button aria-label="Page 2" colorScheme="tertiary">
            2
          </Button>
        </li>
        <li>
          <Button aria-label="Page 3" colorScheme="tertiary">
            3
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 4" colorScheme="tertiary">
            4
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 5" colorScheme="tertiary">
            5
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 6" colorScheme="tertiary">
            6
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 7" colorScheme="tertiary">
            7
          </Button>
        </li>
        <PaginationOverflow className="v-flex v-align-items-center v-mobile-container-hide">
          <VisaOptionHorizontalTiny />
        </PaginationOverflow>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 100" colorScheme="tertiary">
            100
          </Button>
        </li>
        <li>
          <Button aria-label="Go to next page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaChevronRightTiny rtl />
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Go to last page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaArrowEndTiny rtl />
          </Button>
        </li>
      </Pagination>
    </nav>
  );
};

```

### Default pagination with middle page selected
- **Section**: Default paginations
- **URL**: components/pagination/two-digit-pagination
- **Tags**: 
```tsx
import {
  VisaArrowEndTiny,
  VisaArrowStartTiny,
  VisaChevronLeftTiny,
  VisaChevronRightTiny,
  VisaOptionHorizontalTiny,
} from '@visa/nova-icons-react';
import { Button, Pagination, PaginationOverflow } from '@visa/nova-react';

export const TwoDigitPagination = () => {
  return (
    <nav aria-label="2 digit pagination" role="navigation">
      <Pagination className="v-flex v-flex-row v-align-items-center v-gap-4">
        <li className="v-mobile-container-hide">
          <Button aria-label="Go to first page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaArrowStartTiny rtl />
          </Button>
        </li>
        <li>
          <Button aria-label="Go to previous page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaChevronLeftTiny rtl />
          </Button>
        </li>
        <li>
          <Button aria-label="Page 1" className="v-mobile-container-hide" colorScheme="tertiary">
            1
          </Button>
        </li>
        <PaginationOverflow className="v-flex v-align-items-center v-mobile-container-hide">
          <VisaOptionHorizontalTiny />
        </PaginationOverflow>
        <li>
          <Button aria-label="Page 4" colorScheme="tertiary">
            4
          </Button>
        </li>
        <li>
          <Button aria-current="true" aria-label="Page 5" colorScheme="tertiary">
            5
          </Button>
        </li>
        <li>
          <Button aria-label="Page 6" colorScheme="tertiary">
            6
          </Button>
        </li>
        <PaginationOverflow className="v-flex v-align-items-center v-mobile-container-hide">
          <VisaOptionHorizontalTiny />
        </PaginationOverflow>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 100" colorScheme="tertiary">
            100
          </Button>
        </li>
        <li>
          <Button aria-label="Go to next page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaChevronRightTiny rtl />
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Go to last page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaArrowEndTiny rtl />
          </Button>
        </li>
      </Pagination>
    </nav>
  );
};

```

### Default pagination with last page selected
- **Section**: Default paginations
- **URL**: components/pagination/last-page-selected
- **Tags**: 
```tsx
import {
  VisaArrowEndTiny,
  VisaArrowStartTiny,
  VisaChevronLeftTiny,
  VisaChevronRightTiny,
  VisaOptionHorizontalTiny,
} from '@visa/nova-icons-react';
import { Button, Pagination, PaginationOverflow } from '@visa/nova-react';

export const LastDigitPagination = () => {
  return (
    <nav aria-label="1 digit pagination" role="navigation">
      <Pagination className="v-flex v-flex-row v-align-items-center v-gap-4">
        <li className="v-mobile-container-hide">
          <Button aria-label="Go to first page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaArrowStartTiny rtl />
          </Button>
        </li>
        <li>
          <Button aria-label="Go to previous page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaChevronLeftTiny rtl />
          </Button>
        </li>
        <li>
          <Button aria-label="Page 1" colorScheme="tertiary">
            1
          </Button>
        </li>
        <PaginationOverflow className="v-flex v-align-items-center v-mobile-container-hide">
          <VisaOptionHorizontalTiny />
        </PaginationOverflow>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 96" colorScheme="tertiary">
            96
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 97" colorScheme="tertiary">
            97
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 98" colorScheme="tertiary">
            98
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 99" colorScheme="tertiary">
            99
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 100" aria-current="true" colorScheme="tertiary">
            100
          </Button>
        </li>
        <li>
          <Button aria-label="Go to next page" buttonSize="small" colorScheme="tertiary" disabled iconButton>
            <VisaChevronRightTiny rtl />
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Go to last page" buttonSize="small" colorScheme="tertiary" disabled iconButton>
            <VisaArrowEndTiny rtl />
          </Button>
        </li>
      </Pagination>
    </nav>
  );
};

```

### Default slim pagination
- **Section**: Slim paginations
- **URL**: components/pagination/slim-pagination
- **Tags**: 
```tsx
import { VisaChevronLeftTiny, VisaChevronRightTiny } from '@visa/nova-icons-react';
import { Button, Pagination } from '@visa/nova-react';

export const SlimPagination = () => {
  return (
    <nav aria-label="pagination">
      <Pagination className="v-flex v-flex-row v-align-items-center v-gap-4">
        <li>
          <Button aria-label="Go to previous page" buttonSize="small" colorScheme="tertiary" disabled iconButton>
            <VisaChevronLeftTiny rtl />
          </Button>
        </li>
        <li>
          <Button aria-current="true" aria-label="Page 1" colorScheme="tertiary">
            1
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 2" colorScheme="tertiary">
            2
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 3" colorScheme="tertiary">
            3
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 4" colorScheme="tertiary">
            4
          </Button>
        </li>
        <li>
          <Button aria-label="Go to next page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaChevronRightTiny rtl />
          </Button>
        </li>
      </Pagination>
    </nav>
  );
};

```

### Pagination for tables
- **Section**: Custom paginations
- **URL**: components/pagination/table-pagination
- **Tags**: 
```tsx
import {
  VisaArrowEndTiny,
  VisaArrowStartTiny,
  VisaChevronDownTiny,
  VisaChevronLeftTiny,
  VisaChevronRightTiny,
  VisaOptionHorizontalTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  InputContainer,
  InputControl,
  InputMessage,
  Label,
  Pagination,
  PaginationOverflow,
  Select,
  Utility,
  UtilityFragment,
  calculatePagesFromTo,
  calculateTotalPages,
  usePagination,
} from '@visa/nova-react';
import { CSSProperties, FormEvent, useState } from 'react';

const totalItems = 100;

export const TablePagination = () => {
  const [itemsPerPage, setItemsPerPage] = useState(10);

  const totalPages = calculateTotalPages(totalItems, itemsPerPage);
  const {
    isFirstPage,
    isLastPage,
    onFirstPage,
    onLastPage,
    onNextPage,
    onPageChange,
    onPreviousPage,
    pages,
    selectedPage,
  } = usePagination({ totalPages });

  const { from, to } = calculatePagesFromTo(totalItems, itemsPerPage, selectedPage);

  const onItemsPerPageChange = (event: FormEvent<HTMLSelectElement>) => {
    onFirstPage();
    setItemsPerPage(+event.currentTarget.value);
  };

  return (
    <Utility vAlignItems="center" vFlex vFlexRow vFlexWrapReverse vGap={10} vJustifyContent="between">
      <Utility
        style={{ textWrap: 'nowrap' } as CSSProperties}
        tag="fieldset"
        vAlignItems="center"
        vFlex
        vFlexRow
        vGap={12}
      >
        <Label htmlFor="select-items-per-page">Items Per Page</Label>
        <InputContainer>
          <Select
            id="select-items-per-page"
            name="select-items-per-page"
            onChange={onItemsPerPageChange}
            value={itemsPerPage}
          >
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="50">50</option>
          </Select>
          <InputControl>
            <VisaChevronDownTiny />
          </InputControl>
        </InputContainer>
        <InputMessage id="select-default-message">{`${from} - ${to} of ${totalItems}`}</InputMessage>
      </Utility>
      <UtilityFragment>
        <nav aria-label="table pagination" role="navigation">
          <UtilityFragment vAlignItems="center" vFlex vFlexRow vGap={4}>
            <Pagination>
              <li>
                <Button
                  aria-label="Go to first page"
                  buttonSize="small"
                  colorScheme="tertiary"
                  disabled={isFirstPage}
                  iconButton
                  onClick={onFirstPage}
                >
                  <VisaArrowStartTiny rtl />
                </Button>
              </li>
              <li>
                <Button
                  aria-label="Go to previous page"
                  buttonSize="small"
                  colorScheme="tertiary"
                  disabled={isFirstPage}
                  iconButton
                  onClick={onPreviousPage}
                >
                  <VisaChevronLeftTiny rtl />
                </Button>
              </li>
              {pages.map((pageNumber, index) =>
                pageNumber === -1 ? (
                  <UtilityFragment key={`table-pagination-ellipse-${index}`} vAlignItems="center" vFlex>
                    <PaginationOverflow>
                      <VisaOptionHorizontalTiny />
                    </PaginationOverflow>
                  </UtilityFragment>
                ) : (
                  <li key={`table-pagination-page-${pageNumber}`}>
                    <Button
                      aria-current={selectedPage === pageNumber}
                      aria-label={`Page ${pageNumber}`}
                      colorScheme="tertiary"
                      onClick={() => onPageChange(pageNumber as number)}
                    >
                      {pageNumber}
                    </Button>
                  </li>
                )
              )}
              <li>
                <Button
                  aria-label="Go to next page"
                  buttonSize="small"
                  colorScheme="tertiary"
                  disabled={isLastPage}
                  iconButton
                  onClick={onNextPage}
                >
                  <VisaChevronRightTiny rtl />
                </Button>
              </li>
              <li>
                <Button
                  aria-label="Go to last page"
                  buttonSize="small"
                  colorScheme="tertiary"
                  disabled={isLastPage}
                  iconButton
                  onClick={onLastPage}
                >
                  <VisaArrowEndTiny rtl />
                </Button>
              </li>
            </Pagination>
          </UtilityFragment>
        </nav>
      </UtilityFragment>
    </Utility>
  );
};

```

### Pagination with minimum and maximum
- **Section**: Custom paginations
- **URL**: components/pagination/min-max-pagination
- **Tags**: 
```tsx
import {
  VisaArrowEndTiny,
  VisaArrowStartTiny,
  VisaChevronLeftTiny,
  VisaChevronRightTiny,
  VisaOptionHorizontalTiny,
} from '@visa/nova-icons-react';
import { Button, Pagination, PaginationOverflow, UtilityFragment, usePagination } from '@visa/nova-react';

export const MinMaxPagination = () => {
  const {
    isFirstPage,
    isLastPage,
    onFirstPage,
    onLastPage,
    onNextPage,
    onPageChange,
    onPreviousPage,
    pages,
    selectedPage,
  } = usePagination({ maxPageNumber: 75, startPage: 50, totalPages: 100 });

  return (
    <nav aria-label="minimum and maximum pagination" role="navigation">
      <UtilityFragment vAlignItems="center" vFlex vFlexRow vGap={4}>
        <Pagination>
          <li>
            <Button
              aria-label="Go to first page"
              buttonSize="small"
              colorScheme="tertiary"
              disabled={isFirstPage}
              iconButton
              onClick={onFirstPage}
            >
              <VisaArrowStartTiny rtl />
            </Button>
          </li>
          <li>
            <Button
              aria-label="Go to previous page"
              buttonSize="small"
              colorScheme="tertiary"
              disabled={isFirstPage}
              iconButton
              onClick={onPreviousPage}
            >
              <VisaChevronLeftTiny rtl />
            </Button>
          </li>
          {pages.map((pageNumber, index) =>
            pageNumber === -1 ? (
              <UtilityFragment key={`min-max-pagination-ellipse-${index}`} vAlignItems="center" vFlex>
                <PaginationOverflow>
                  <VisaOptionHorizontalTiny />
                </PaginationOverflow>
              </UtilityFragment>
            ) : (
              <li key={`min-max-pagination-page-${pageNumber}`}>
                <Button
                  aria-current={selectedPage === pageNumber}
                  aria-label={`Page ${pageNumber}`}
                  colorScheme="tertiary"
                  onClick={() => onPageChange(pageNumber as number)}
                >
                  {pageNumber}
                </Button>
              </li>
            )
          )}
          <li>
            <Button
              aria-label="Go to next page"
              buttonSize="small"
              colorScheme="tertiary"
              disabled={isLastPage}
              iconButton
              onClick={onNextPage}
            >
              <VisaChevronRightTiny rtl />
            </Button>
          </li>
          <li>
            <Button
              aria-label="Go to last page"
              buttonSize="small"
              colorScheme="tertiary"
              disabled={isLastPage}
              iconButton
              onClick={onLastPage}
            >
              <VisaArrowEndTiny rtl />
            </Button>
          </li>
        </Pagination>
      </UtilityFragment>
    </nav>
  );
};

```

## Property Sections
### Pagination
- **Selector**: <Pagination />
- **Description**: Set of links used to navigate content split across multiple pages.

### PaginationOverflow
- **Selector**: <PaginationOverflow />
- **Description**: Element to show hidden elements within pagination component, usually used with ellipsis icon.

### usePagination
- **Selector**: None
- **Description**: This hook is used to manage pagination events, state, and visible page blocks.

## Properties
### ref
- **Section**: Pagination
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Pagination
- **Type**: ElementType
- **Default**: ul
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: PaginationOverflow
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: PaginationOverflow
- **Type**: ElementType
- **Default**: li
- **Required**: false
- **Description**: Tag of Component

