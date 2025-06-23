# tabs

## Metadata
- **Version**: 0.0.1
- **Description**: Organizational element that separates content and allows users to switch between views.
- **Category**: components

## Example Sections
1. **Vertical tabs**
   - Description: 
2. **Horizontal tabs**
   - Description: 
3. **Stacked Tabs**
   - Description: 
4. **Custom tabs**
   - Description: 

## Examples
### Default vertical tablist
- **Section**: Vertical tabs
- **URL**: components/tabs/default-vertical-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, UtilityFragment, useTabs } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-vertical-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
  },
];

export const DefaultVerticalTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'vertical', defaultSelected: 0 });

  return (
    <Utility vFlex vFlexWrap vGap={8}>
      <Tabs onKeyDown={onKeyNavigation} orientation="vertical" role="tablist" style={{ flexBasis: '30%' }}>
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              tabIndex={getTabIndex(index)}
            >
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vFlex vFlexGrow vElevation="inset">
        <UtilityFragment vPadding={10}>
          <Surface id={tabsContent[selectedIndex].id} role="tabpanel">
            <span>{tabsContent[selectedIndex]?.text}</span>
          </Surface>
        </UtilityFragment>
      </Utility>
    </Utility>
  );
};

```

### Vertical tablist with icon
- **Section**: Vertical tabs
- **URL**: components/tabs/icon-vertical-tabs
- **Tags**: 
```tsx
import { VisaStatisticsTiny, VisaTopicTiny, VisaEmailTiny, VisaHomeTiny } from '@visa/nova-icons-react';
import { Button, Surface, Tab, Tabs, Utility, UtilityFragment, useTabs } from '@visa/nova-react';
import { CSSProperties } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-icon-vertical-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    icon: <VisaStatisticsTiny />,
    id: `${id}-tab-0`,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    icon: <VisaTopicTiny />,
    id: `${id}-tab-1`,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    icon: <VisaEmailTiny />,
    id: `${id}-tab-2`,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    icon: <VisaHomeTiny />,
    id: `${id}-tab-3`,
  },
];

export const IconVerticalTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'vertical', defaultSelected: 0 });

  return (
    <Utility vFlex vFlexWrap vGap={8}>
      <Tabs onKeyDown={onKeyNavigation} orientation="vertical" role="tablist" style={{ flexBasis: '30%' }}>
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              tabIndex={getTabIndex(index)}
              style={{ minInlineSize: 'max-content' } as CSSProperties}
            >
              {tabContent.icon}
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vFlex vFlexGrow vElevation="inset">
        <UtilityFragment vPadding={10}>
          <Surface id={tabsContent[selectedIndex].id} role="tabpanel">
            <span>{tabsContent[selectedIndex]?.text}</span>
          </Surface>
        </UtilityFragment>
      </Utility>
    </Utility>
  );
};

```

### Vertical tablist with disabled tab
- **Section**: Vertical tabs
- **URL**: components/tabs/disabled-vertical-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, UtilityFragment, useTabs } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-disabled-vertical-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
    disabled: true,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
  },
];

export const DisabledVerticalTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'vertical', defaultSelected: 0 });

  return (
    <Utility vFlex vFlexWrap vGap={8}>
      <Tabs onKeyDown={onKeyNavigation} orientation="vertical" role="tablist" style={{ flexBasis: '30%' }}>
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              disabled={tabContent.disabled}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              tabIndex={getTabIndex(index)}
            >
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vFlex vFlexGrow vElevation="inset">
        <UtilityFragment vPadding={10}>
          <Surface id={tabsContent[selectedIndex].id} role="tabpanel">
            <span>{tabsContent[selectedIndex]?.text}</span>
          </Surface>
        </UtilityFragment>
      </Utility>
    </Utility>
  );
};

```

### Vertical tab with menu
- **Section**: Vertical tabs
- **URL**: components/tabs/vertical-tab-with-menu
- **Tags**: 
```tsx
import { Button, Tab, Tabs, TabSuffix, Utility } from '@visa/nova-react';
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaHomeTiny } from '@visa/nova-icons-react';
import { useState } from 'react';

const subItems = ['L1 label 1', 'L1 label 2'];

export const VerticalTabWithMenu = () => {
  const [isTabExpanded, setIsTabExpanded] = useState(false);

  return (
    <Utility vFlex vFlexWrap vGap={8}>
      <Tabs orientation="vertical" tag="div">
        <Tab tag="div">
          <Button aria-expanded={isTabExpanded} colorScheme="tertiary" onClick={() => setIsTabExpanded(!isTabExpanded)}>
            <VisaHomeTiny /> Label
            <TabSuffix element={isTabExpanded ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
          </Button>
          {isTabExpanded && (
            <Tabs orientation="vertical">
              {subItems.map((subItem, i) => (
                <Tab key={i}>
                  <Button colorScheme="tertiary">{subItem}</Button>
                </Tab>
              ))}
            </Tabs>
          )}
        </Tab>
      </Tabs>
    </Utility>
  );
};

```

### Default horizontal tab
- **Section**: Horizontal tabs
- **URL**: components/tabs/default-horizontal-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, useTabs } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-horizontal-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
  },
];

export const DefaultHorizontalTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'horizontal', defaultSelected: 0 });

  return (
    <Utility>
      <Tabs onKeyDown={onKeyNavigation} role="tablist">
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              tabIndex={getTabIndex(index)}
            >
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vMarginVertical={8} vFlex vFlexGrow vElevation="inset">
        <Surface id={tabsContent[selectedIndex].id} role="tabpanel" style={{ minBlockSize: '200px' }}>
          <span>{tabsContent[selectedIndex]?.text}</span>
        </Surface>
      </Utility>
    </Utility>
  );
};

```

### Horizontal tab with icon
- **Section**: Horizontal tabs
- **URL**: components/tabs/icon-horizontal-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, useTabs } from '@visa/nova-react';
import { VisaStatisticsTiny, VisaTopicTiny, VisaEmailTiny, VisaHomeTiny } from '@visa/nova-icons-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-icon-horizontal-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
    icon: <VisaStatisticsTiny />,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
    icon: <VisaTopicTiny />,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
    icon: <VisaEmailTiny />,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
    icon: <VisaHomeTiny />,
  },
];

export const IconHorizontalTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'horizontal', defaultSelected: 0 });

  return (
    <Utility>
      <Tabs onKeyDown={onKeyNavigation} role="tablist">
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              tabIndex={getTabIndex(index)}
            >
              {tabContent.icon}
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vMarginVertical={8} vFlex vFlexGrow vElevation="inset">
        <Surface id={tabsContent[selectedIndex].id} role="tabpanel" style={{ minBlockSize: '200px' }}>
          <span>{tabsContent[selectedIndex]?.text}</span>
        </Surface>
      </Utility>
    </Utility>
  );
};

```

### Horizontal tablist with disabled tab
- **Section**: Horizontal tabs
- **URL**: components/tabs/disabled-horizontal-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, useTabs } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-disabled-horizontal-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
    disabled: true,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
  },
];

export const DisabledHorizontalTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'horizontal', defaultSelected: 0 });

  return (
    <Utility>
      <Tabs onKeyDown={onKeyNavigation} role="tablist">
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              disabled={tabContent.disabled}
              role="tab"
              tabIndex={getTabIndex(index)}
            >
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vMarginVertical={8} vFlex vFlexGrow vElevation="inset">
        <Surface id={tabsContent[selectedIndex].id} role="tabpanel" style={{ minBlockSize: '200px' }}>
          <span>{tabsContent[selectedIndex]?.text}</span>
        </Surface>
      </Utility>
    </Utility>
  );
};

```

### Horizontal tab with menu
- **Section**: Horizontal tabs
- **URL**: components/tabs/horizontal-tab-with-menu
- **Tags**: 
```tsx
import { useClick, useFloating, useInteractions } from '@floating-ui/react';
import { useState } from 'react';
import { DropdownButton, DropdownMenu, Listbox, ListboxItem, Utility, Tab, TabSuffix } from '@visa/nova-react';
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaHomeTiny } from '@visa/nova-icons-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-horizontal-tabs-with-menu-example';

export const HorizontalTabWithMenu = () => {
  const [open, setOpen] = useState(false);

  const { context, floatingStyles, refs } = useFloating({
    open,
    onOpenChange: setOpen,
    placement: 'bottom-start',
  });

  const onClick = useClick(context);

  const { getReferenceProps, getFloatingProps } = useInteractions([onClick]);

  return (
    <Tab tag="div" style={{ blockSize: 150 }}>
      <DropdownButton
        aria-controls={id}
        aria-expanded={open}
        colorScheme="tertiary"
        buttonSize="large"
        id={`${id}-button`}
        ref={refs.setReference}
        {...getReferenceProps()}
      >
        <VisaHomeTiny /> Label
        {open ? <TabSuffix element={<VisaChevronUpTiny />} /> : <TabSuffix element={<VisaChevronDownTiny />} />}
      </DropdownButton>
      {open && (
        <DropdownMenu
          id={id}
          ref={refs.setFloating}
          style={{ maxInlineSize: '100%', inlineSize: '180px', ...floatingStyles }}
          {...getFloatingProps()}
        >
          <Listbox tag="div">
            <Utility
              element={<ListboxItem tag="button" />}
              vPaddingHorizontal={8}
              vPaddingRight={24}
              vPaddingVertical={11}
            >
              Label 1
            </Utility>
            <Utility
              element={<ListboxItem tag="button" />}
              vPaddingHorizontal={8}
              vPaddingRight={24}
              vPaddingVertical={11}
            >
              Label 2
            </Utility>
          </Listbox>
        </DropdownMenu>
      )}
    </Tab>
  );
};

```

### Default stacked tablist
- **Section**: Stacked Tabs
- **URL**: components/tabs/default-stacked-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, useTabs } from '@visa/nova-react';

import { VisaStatisticsLow, VisaEmailLow, VisaReceiptLow, VisaHomeLow } from '@visa/nova-icons-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-stacked-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
    icon: <VisaHomeLow />,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
    icon: <VisaReceiptLow />,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
    icon: <VisaStatisticsLow />,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
    icon: <VisaEmailLow />,
  },
];

export const DefaultStackedTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'horizontal', defaultSelected: 0 });

  return (
    <Utility>
      <Tabs onKeyDown={onKeyNavigation} role="tablist">
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              stacked
              tabIndex={getTabIndex(index)}
            >
              {tabContent.icon}
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vMarginVertical={8} vFlex vFlexGrow vElevation="inset">
        <Surface id={tabsContent[selectedIndex]?.id} role="tabpanel" style={{ minBlockSize: '200px' }}>
          <span>{tabsContent[selectedIndex]?.text}</span>
        </Surface>
      </Utility>
    </Utility>
  );
};

```

### Stacked tablist with disabled tab
- **Section**: Stacked Tabs
- **URL**: components/tabs/disabled-stacked-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, useTabs } from '@visa/nova-react';
import { VisaStatisticsLow, VisaEmailLow, VisaReceiptLow, VisaHomeLow } from '@visa/nova-icons-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-disabled-stacked-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
    icon: <VisaHomeLow />,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
    icon: <VisaReceiptLow />,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
    icon: <VisaStatisticsLow />,
    disabled: true,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
    icon: <VisaEmailLow />,
  },
];

export const DisabledStackedTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'horizontal', defaultSelected: 0 });

  return (
    <Utility>
      <Tabs onKeyDown={onKeyNavigation} role="tablist">
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              disabled={tabContent.disabled}
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              stacked
              tabIndex={getTabIndex(index)}
            >
              {tabContent.icon}
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vMarginVertical={8} vFlex vFlexGrow vElevation="inset">
        <Surface id={tabsContent[selectedIndex]?.id} role="tabpanel" style={{ minBlockSize: '200px' }}>
          <span>{tabsContent[selectedIndex]?.text}</span>
        </Surface>
      </Utility>
    </Utility>
  );
};

```

### Stacked tabs with notifications
- **Section**: Stacked Tabs
- **URL**: components/tabs/stacked-tabs-with-notifications
- **Tags**: 
```tsx
import { Badge, Button, Surface, Tab, Tabs, Utility, useTabs } from '@visa/nova-react';
import { VisaStatisticsLow, VisaEmailLow, VisaReceiptLow, VisaHomeLow } from '@visa/nova-icons-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-notifications-stacked-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
    icon: <VisaHomeLow />,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
    icon: <VisaReceiptLow />,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
    icon: <VisaStatisticsLow />,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
    icon: <VisaEmailLow />,
  },
];

export const StackedTabsWithNotifications = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'horizontal', defaultSelected: 0 });

  return (
    <Utility>
      <Tabs onKeyDown={onKeyNavigation} role="tablist">
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              stacked
              tabIndex={getTabIndex(index)}
            >
              {tabContent.icon}
              {tabContent.tabLabel}
              <Badge
                tag="sup"
                aria-label={`${index + 1} unread notification${index === 0 ? '' : 's'}`}
                badgeVariant="number"
              >
                {index + 1}
              </Badge>
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vMarginVertical={8} vFlex vFlexGrow vElevation="inset">
        <Surface id={tabsContent[selectedIndex]?.id} role="tabpanel" style={{ minBlockSize: '200px' }}>
          <span>{tabsContent[selectedIndex]?.text}</span>
        </Surface>
      </Utility>
    </Utility>
  );
};

```

### Alternate horizontal tablist
- **Section**: Custom tabs
- **URL**: components/tabs/alternate-horizontal-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, useTabs } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-alternate-horizontal-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
  },
];

export const AlternateHorizontalTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'horizontal', defaultSelected: 0 });

  return (
    <Surface surfaceType="alternate">
      <Tabs onKeyDown={onKeyNavigation} role="tablist">
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              tabIndex={getTabIndex(index)}
            >
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vMarginVertical={8} vFlex vFlexGrow vElevation="xxlarge">
        {/*
          We have a nested surface that has been styled in our app's stylesheet. 
          This has been done to leverage darker palette variables and bring contrast to this custom tabpanel.

          The CSS rule is something like this:

          .v-surface.v-alternate .v-surface {
            // The background color is set to surface-3 of the default palette.
            background: var(--palette-default-surface-3);
          }
        */}
        <Surface id={tabsContent[selectedIndex].id} role="tabpanel" style={{ minBlockSize: '200px' }}>
          <span>{tabsContent[selectedIndex]?.text}</span>
        </Surface>
      </Utility>
    </Surface>
  );
};

```

### Alternate vertical tablist
- **Section**: Custom tabs
- **URL**: components/tabs/alternate-vertical-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, useTabs } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-alternate-vertical-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
  },
];

export const AlternateVerticalTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'vertical', defaultSelected: 0 });

  return (
    <Surface surfaceType="alternate">
      <Utility vFlex vFlexWrap vGap={8}>
        <Tabs orientation="vertical" onKeyDown={onKeyNavigation} role="tablist" style={{ flexBasis: '30%' }}>
          {tabsContent.map((tabContent, index) => (
            <Tab key={tabContent.id} role="none">
              <Button
                aria-selected={index === selectedIndex}
                aria-controls={tabContent.id}
                colorScheme="tertiary"
                onClick={() => onIndexChange(index)}
                ref={el => {
                  tabsRef.current[index] = el;
                }}
                role="tab"
                tabIndex={getTabIndex(index)}
              >
                {tabContent.tabLabel}
              </Button>
            </Tab>
          ))}
        </Tabs>
        <Utility vFlex vFlexGrow vElevation="xxlarge">
          {/*
          We have a nested surface that has been styled in our app's stylesheet. 
          This has been done to leverage darker palette variables and bring contrast to this custom tabpanel.

          The CSS rule is something like this:

          .v-surface.v-alternate .v-surface {
            // The background color is set to surface-3 of the default palette.
            background: var(--palette-default-surface-3);
          }
        */}
          <Surface id={tabsContent[selectedIndex].id} role="tabpanel" style={{ minBlockSize: '200px' }}>
            <span>{tabsContent[selectedIndex]?.text}</span>
          </Surface>
        </Utility>
      </Utility>
    </Surface>
  );
};

```

### Alternate stacked tablist
- **Section**: Custom tabs
- **URL**: components/tabs/alternate-stacked-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, useTabs } from '@visa/nova-react';
import { VisaStatisticsLow, VisaEmailLow, VisaReceiptLow, VisaHomeLow } from '@visa/nova-icons-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-alternate-stacked-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
    icon: <VisaHomeLow />,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
    icon: <VisaReceiptLow />,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
    icon: <VisaStatisticsLow />,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
    icon: <VisaEmailLow />,
  },
];

export const AlternateStackedTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'horizontal', defaultSelected: 0 });

  return (
    <Surface surfaceType="alternate">
      <Utility>
        <Tabs onKeyDown={onKeyNavigation} role="tablist">
          {tabsContent.map((tabContent, index) => (
            <Tab key={`default-stacked-tab-${index}`} role="none">
              <Button
                aria-selected={index === selectedIndex}
                aria-controls={tabContent.id}
                colorScheme="tertiary"
                onClick={() => onIndexChange(index)}
                ref={el => {
                  tabsRef.current[index] = el;
                }}
                role="tab"
                stacked
                tabIndex={getTabIndex(index)}
              >
                {tabContent.icon}
                {tabContent.tabLabel}
              </Button>
            </Tab>
          ))}
        </Tabs>
        <Utility vMarginVertical={8} vFlex vFlexGrow vElevation="xxlarge">
          {/*
          We have a nested surface that has been styled in our app's stylesheet. 
          This has been done to leverage darker palette variables and bring contrast to this custom tabpanel.

          The CSS rule is something like this:

          .v-surface.v-alternate .v-surface {
            // The background color is set to surface-3 of the default palette.
            background: var(--palette-default-surface-3);
          }
        */}
          <Surface id={tabsContent[selectedIndex]?.id} role="tabpanel" style={{ minBlockSize: '200px' }}>
            <span>{tabsContent[selectedIndex]?.text}</span>
          </Surface>
        </Utility>
      </Utility>
    </Surface>
  );
};

```

### Tablist with automatic activation
- **Section**: Custom tabs
- **URL**: components/tabs/auto-horizontal-tabs
- **Tags**: 
```tsx
import { Button, Surface, Tab, Tabs, Utility, useTabs } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-auto-horizontal-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
  },
];

export const AutoHorizontalTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ autoSelect: true, arrowKeyNavigation: 'horizontal', defaultSelected: 0 });

  return (
    <Utility>
      <Tabs onKeyDown={onKeyNavigation} role="tablist">
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              tabIndex={getTabIndex(index)}
            >
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vMarginVertical={8} vFlex vFlexGrow vElevation="inset">
        <Surface id={tabsContent[selectedIndex].id} role="tabpanel" style={{ minBlockSize: '200px' }}>
          <span>{tabsContent[selectedIndex]?.text}</span>
        </Surface>
      </Utility>
    </Utility>
  );
};

```

## Property Sections
### Tabs
- **Selector**: <Tabs />
- **Description**: Organizational element that separates content and allows users to switch between views.

### Tab
- **Selector**: <Tab />
- **Description**: Singular tab component to be used in a tab group.

### TabSuffix
- **Selector**: <TabSuffix />
- **Description**: Utility class for positioning and styling elements at the end of tab components.

### useTabs
- **Selector**: None
- **Description**: This hook allows us to set the <defaultSelected> value, which indicates that we are selecting that item by default.

## Properties
### ref
- **Section**: Tabs
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### stacked
- **Section**: Tabs
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Stacked

### tag
- **Section**: Tabs
- **Type**: ElementType
- **Default**: ul
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: Tab
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### sectionTitle
- **Section**: Tab
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: section title

### tag
- **Section**: Tab
- **Type**: ElementType
- **Default**: li
- **Required**: false
- **Description**: Tag of Component

### element
- **Section**: TabSuffix
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with children)

### ref
- **Section**: TabSuffix
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

