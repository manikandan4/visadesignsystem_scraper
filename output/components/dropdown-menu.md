# dropdown-menu

## Metadata
- **Version**: 0.0.1
- **Description**: Interactive element enabling users to select a single option from a list.
- **Category**: components

## Example Sections
1. **Text button dropdown menus**
   - Description: 
2. **Icon button dropdown menus**
   - Description: 
3. **Custom dropdown menus**
   - Description: 

## Examples
### Default text button dropdown menu
- **Section**: Text button dropdown menus
- **URL**: components/dropdown-menu/default-dropdown-menu
- **Tags**: 
```tsx
import { useClick, useFloating, useInteractions } from '@floating-ui/react';
import { VisaChevronDownTiny, VisaChevronUpTiny } from '@visa/nova-icons-react';
import { useState } from 'react';
import { Button, DropdownButton, DropdownMenu, Listbox, UtilityFragment } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'dropdown-menu-default';

export const DefaultDropdownMenu = () => {
  const [open, setOpen] = useState(false);

  const { context, floatingStyles, refs } = useFloating({
    open,
    onOpenChange: setOpen,
    placement: 'bottom-start',
  });

  const onClick = useClick(context);

  const { getReferenceProps, getFloatingProps } = useInteractions([onClick]);

  return (
    // This div is not required, it's used to show the whole dropdown menu in the example
    <div style={{ blockSize: 250 }}>
      <DropdownButton
        aria-controls={id}
        aria-expanded={open}
        id={`${id}-button`}
        ref={refs.setReference}
        {...getReferenceProps()}
      >
        Action
        {open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
      </DropdownButton>
      {open && (
        <DropdownMenu
          id={id}
          aria-hidden={!open}
          ref={refs.setFloating}
          style={{ inlineSize: '180px', ...floatingStyles }}
          {...getFloatingProps()}
        >
          <UtilityFragment vHide={!open}>
            <Listbox>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    Label 1
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    Label 3
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    Label 3
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary">
                    Label 4
                  </Button>
                </UtilityFragment>
              </li>
            </Listbox>
          </UtilityFragment>
        </DropdownMenu>
      )}
    </div>
  );
};

```

### Default icon button dropdown menu
- **Section**: Icon button dropdown menus
- **URL**: components/dropdown-menu/icon-dropdown-menu
- **Tags**: 
```tsx
import { useClick, useFloating, useInteractions } from '@floating-ui/react';
import { VisaOptionHorizontalHigh } from '@visa/nova-icons-react';
import { useState } from 'react';
import { Button, DropdownButton, DropdownMenu, Listbox, UtilityFragment } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'dropdown-menu-icon';

export const IconDropdownMenu = () => {
  const [open, setOpen] = useState(false);

  const { context, floatingStyles, refs } = useFloating({
    open,
    onOpenChange: setOpen,
    placement: 'bottom-start',
  });

  const onClick = useClick(context);

  const { getReferenceProps, getFloatingProps } = useInteractions([onClick]);

  return (
    // This div is not required, it's used to show the whole dropdown menu in the example
    <div style={{ blockSize: 250 }}>
      <DropdownButton
        aria-controls={id}
        aria-expanded={open}
        aria-label="see more options"
        iconButton
        id={`${id}-button`}
        ref={refs.setReference}
        {...getReferenceProps()}
      >
        <VisaOptionHorizontalHigh />
      </DropdownButton>
      {open && (
        <DropdownMenu
          id={id}
          aria-hidden={!open}
          ref={refs.setFloating}
          style={{ inlineSize: '180px', ...floatingStyles }}
          {...getFloatingProps()}
        >
          <UtilityFragment vHide={!open}>
            <Listbox>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    Label 1
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    Label 2
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    Label 2
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    Label 4
                  </Button>
                </UtilityFragment>
              </li>
            </Listbox>
          </UtilityFragment>
        </DropdownMenu>
      )}
    </div>
  );
};

```

### Dropdown menu with tabs
- **Section**: Custom dropdown menus
- **URL**: components/dropdown-menu/dropdown-menu-with-tabs
- **Tags**: 
```tsx
import { useClick, useFloating, useInteractions } from '@floating-ui/react';
import { VisaOptionHorizontalHigh } from '@visa/nova-icons-react';
import { Button, DropdownButton, DropdownMenu, Tab, Tabs, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'dropdown-menu-with-tabs';

export const DropdownMenuWithTabs = () => {
  const [open, setOpen] = useState(false);

  const { context, floatingStyles, refs } = useFloating({
    open,
    onOpenChange: setOpen,
    placement: 'bottom-start',
  });

  const onClick = useClick(context);

  const { getReferenceProps, getFloatingProps } = useInteractions([onClick]);

  return (
    // This div is not required, it's used to show the whole dropdown menu in the example
    <div style={{ blockSize: 250 }}>
      <DropdownButton
        aria-controls={id}
        aria-expanded={open}
        aria-label="see more options"
        iconButton
        id={`${id}-button`}
        ref={refs.setReference}
        {...getReferenceProps()}
      >
        <VisaOptionHorizontalHigh />
      </DropdownButton>
      {open && (
        <DropdownMenu
          id={id}
          ref={refs.setFloating}
          style={{ inlineSize: 'max-content', ...floatingStyles }}
          {...getFloatingProps()}
        >
          <UtilityFragment vGap={4} vPaddingVertical={7} vPaddingRight={8} vHide={!open}>
            <Tabs orientation="vertical" role="tablist">
              <Tab role="none">
                <Button aria-selected="false" colorScheme="tertiary" role="tab">
                  Label 1
                </Button>
              </Tab>
              <Tab role="none">
                <Button aria-selected="true" colorScheme="tertiary" role="tab">
                  Label 2
                </Button>
              </Tab>
              <Tab role="none">
                <Button aria-selected="false" colorScheme="tertiary" role="tab">
                  Label 3
                </Button>
              </Tab>
              <Tab role="none">
                <Button aria-selected="false" colorScheme="tertiary" role="tab">
                  Label 4
                </Button>
              </Tab>
            </Tabs>
          </UtilityFragment>
        </DropdownMenu>
      )}
    </div>
  );
};

```

### Dropdown menu with leading icons and destructive action
- **Section**: Custom dropdown menus
- **URL**: components/dropdown-menu/dropdown-menu-with-leading-icons
- **Tags**: 
```tsx
import { useClick, useFloating, useInteractions } from '@floating-ui/react';
import {
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaDeleteTiny,
  VisaExportTiny,
  VisaFileDownloadTiny,
} from '@visa/nova-icons-react';
import { Button, DropdownButton, DropdownMenu, Listbox, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'dropdown-menu-with-leading-icons';

export const DropdownMenuWithLeadingIcons = () => {
  const [open, setOpen] = useState(false);

  const { context, floatingStyles, refs } = useFloating({
    open,
    onOpenChange: setOpen,
    placement: 'bottom-start',
  });

  const onClick = useClick(context);

  const { getReferenceProps, getFloatingProps } = useInteractions([onClick]);

  return (
    // This div is not required, it's used to show the whole dropdown menu in the example
    <div style={{ blockSize: 250 }}>
      <DropdownButton
        aria-controls={id}
        aria-expanded={open}
        id={`${id}-button`}
        ref={refs.setReference}
        {...getReferenceProps()}
      >
        Action
        {open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
      </DropdownButton>
      {open && (
        <DropdownMenu
          id={id}
          aria-hidden={!open}
          ref={refs.setFloating}
          style={{ inlineSize: '180px', ...floatingStyles }}
          {...getFloatingProps()}
        >
          <UtilityFragment vHide={!open}>
            <Listbox>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    <VisaExportTiny /> Label 1
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    <VisaFileDownloadTiny /> Label 3
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    <VisaFileDownloadTiny /> Label 3
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" destructive>
                    <VisaDeleteTiny /> Label 4
                  </Button>
                </UtilityFragment>
              </li>
            </Listbox>
          </UtilityFragment>
        </DropdownMenu>
      )}
    </div>
  );
};

```

## Property Sections
### DropdownMenu
- **Selector**: <DropdownMenu />
- **Description**: Interactive element enabling users to select a single option from a list.

### DropdownButton
- **Selector**: <DropdownButton />
- **Description**: Button used to hide or show the dropdown menu.

### DropdownContainer
- **Selector**: <DropdownContainer />
- **Description**: Container that styles the dropdown menu.

## Properties
### ref
- **Section**: DropdownMenu
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: DropdownMenu
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Scroll

### alternate
- **Section**: DropdownButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate color scheme

### buttonSize
- **Section**: DropdownButton
- **Type**: "small" , "large"
- **Default**: 
- **Required**: false
- **Description**: Size of Button

### colorScheme
- **Section**: DropdownButton
- **Type**: "secondary" , "tertiary"
- **Default**: 
- **Required**: false
- **Description**: Color Scheme of Button

### destructive
- **Section**: DropdownButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Destructive Button

### element
- **Section**: DropdownButton
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### iconButton
- **Section**: DropdownButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Button

### iconTwoColor
- **Section**: DropdownButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Two Button

### ref
- **Section**: DropdownButton
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### stacked
- **Section**: DropdownButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Stacked Button

### subtle
- **Section**: DropdownButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Subtle Button

### tag
- **Section**: DropdownButton
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag (not compatible with element property)

### ref
- **Section**: DropdownContainer
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: DropdownContainer
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of the component

