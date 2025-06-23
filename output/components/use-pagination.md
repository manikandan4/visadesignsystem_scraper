# use-pagination

## Metadata
- **Version**: 0.0.1
- **Description**: This hook is used to manage pagination events, state, and visible page blocks.
- **Category**: hooks

## Example Sections
1. **Behavior and usage**
   - Description: 

## Examples
### 
- **Section**: Behavior and usage
- **URL**: hooks/use-pagination/use-pagination-example
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

export const UsePaginationExample = () => {
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
  } = usePagination({ maxPageNumber: 10, startPage: 1, totalPages: 12 });

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

