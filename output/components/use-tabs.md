# use-tabs

## Metadata
- **Version**: 0.0.1
- **Description**: This hook allows us to set the <defaultSelected> value, which indicates that we are selecting that item by default.
- **Category**: hooks

## Example Sections
1. **Behavior and usage**
   - Description: 

## Examples
### 
- **Section**: Behavior and usage
- **URL**: hooks/use-tabs/use-tabs-example
- **Tags**: 
```tsx
import { Button, Tab, Tabs, useTabs } from '@visa/nova-react';

const tabsList = ['Tab 1', 'Tab 2', 'Tab 3'];

export const UseTabsExample = () => {
  const { getTabIndex, onIndexChange, onKeyNavigation, ref: tabsRef, selectedIndex } = useTabs();

  return (
    <Tabs onKeyDown={onKeyNavigation} role="tablist">
      {tabsList.map((tab, index) => (
        <Tab key={`use-tabs-horizontal-tab-${index}`} role="none">
          <Button
            aria-selected={index === selectedIndex}
            buttonSize="large"
            colorScheme="tertiary"
            onClick={() => onIndexChange(index)}
            ref={el => {
              tabsRef.current[index] = el;
            }}
            role="tab"
            tabIndex={getTabIndex(index)}
          >
            {tab}
          </Button>
        </Tab>
      ))}
    </Tabs>
  );
};

```

