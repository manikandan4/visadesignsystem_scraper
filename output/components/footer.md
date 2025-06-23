# footer

## Metadata
- **Version**: 0.0.1
- **Description**: Content anchored at the bottom of a page to provide important information or links.
- **Category**: components

## Example Sections
1. **Examples**
   - Description: 

## Examples
### Default footer
- **Section**: Examples
- **URL**: components/footer/default-footer
- **Tags**: docs
```tsx
// If you are using Vite to run your application, please follow the instruction on the top of the page.
import { Footer, Link, Utility, VisaLogo } from '@visa/nova-react';

export const DefaultFooter = () => {
  return (
    <Footer className="v-gap-15">
      <Utility vFlex vMarginRight={1}>
        <VisaLogo aria-label="Visa" />
      </Utility>
      <Utility vFlex vFlexWrap vFlexGrow vJustifyContent="between" vGap={42}>
        {`Copyright © ${new Date().getFullYear()} Visa Inc. All Rights Reserved`}
        <Utility tag="ul" vFlex vFlexWrap vGap={16}>
          <li>
            <Link href="/footer">Contact us</Link>
          </li>
          <li>
            <Link href="/footer">Privacy</Link>
          </li>
          <li>
            <Link href="/footer">Legal/terms and conditions</Link>
          </li>
        </Utility>
      </Utility>
    </Footer>
  );
};

```

### Navigational footer
- **Section**: Examples
- **URL**: components/footer/navigational-footer
- **Tags**: docs
```tsx
// If you are using Vite to run your application, please follow the instruction on the top of the page.
import { Footer, Link, Typography, Utility, UtilityFragment, VisaLogo } from '@visa/nova-react';

export const NavigationalFooter = () => {
  return (
    <UtilityFragment vFlex vFlexRow vGap={24} vPadding={24}>
      <Footer>
        <Utility vFlex vFlexCol vFlexGrow vFlexShrink0 vGap={24} style={{ flexBasis: 'calc(30% - 32px)' }}>
          <VisaLogo aria-label="Visa" />
          <p>
            The information furnished here is confidential and to be used solely for the support of clients' Visa
            programs. This information shall not be duplicated, published, or disclosed, in whole or in part, without
            the prior written permission of Visa.
          </p>
          <Typography colorScheme="subtle">Copyright &copy; YYYY-YYYY Visa. All rights reserved.</Typography>
        </Utility>
        <Utility vFlex vFlexGrow vFlexWrap vGap={24}>
          <Utility vFlex vFlexCol vFlexGrow vGap={24} style={{ flexBasis: 'calc(15% - 32px)' }}>
            <Typography tag="h2" variant="body-2-bold">
              Visa Inc.
            </Typography>
            <Utility tag="ul" vFlex vFlexCol vGap={16}>
              <li>
                <Link href="./footer">Privacy</Link>
              </li>
              <li>
                <Link href="./footer">Terms of use</Link>
              </li>
              <li>
                <Link href="./footer">About Visa</Link>
              </li>
            </Utility>
          </Utility>
          <Utility vFlex vFlexCol vFlexGrow vGap={24} style={{ flexBasis: 'calc(15% - 32px)' }}>
            <Typography tag="h2" variant="body-2-bold">
              Support
            </Typography>
            <Utility tag="ul" vFlex vFlexCol vGap={16}>
              <li>
                <Link href="./footer">FAQs</Link>
              </li>
              <li>
                <Link href="./footer">Feedback/Contact Us</Link>
              </li>
              <li>
                <Link href="./footer">Online help</Link>
              </li>
            </Utility>
          </Utility>
          <Utility vFlex vFlexCol vFlexGrow vGap={24} style={{ flexBasis: 'calc(15% - 32px)' }}>
            <Typography tag="h2" variant="body-2-bold">
              Update profile
            </Typography>
            <Utility tag="ul" vFlex vFlexCol vGap={16}>
              <li>
                <Link href="./footer">My information</Link>
              </li>
              <li>
                <Link href="./footer">My security</Link>
              </li>
              <li>
                <Link href="./footer">My services</Link>
              </li>
            </Utility>
          </Utility>
          <Utility vFlex vFlexCol vFlexGrow vGap={24} style={{ flexBasis: 'calc(15% - 32px)' }}>
            <Typography tag="h2" variant="body-2-bold">
              Site index
            </Typography>
            <Utility tag="ul" vFlex vFlexCol vGap={16}>
              <li>
                <Link href="./footer">Alphabetized index</Link>
              </li>
              <li>
                <Link href="./footer">Site map</Link>
              </li>
              <li>
                <Link href="./footer">Topic index</Link>
              </li>
            </Utility>
          </Utility>
        </Utility>
      </Footer>
    </UtilityFragment>
  );
};

```

## Property Sections
### Footer
- **Selector**: <Footer />
- **Description**: Content anchored at the bottom of a page to provide important information or links.

## Properties
### ref
- **Section**: Footer
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Footer
- **Type**: ElementType
- **Default**: footer
- **Required**: false
- **Description**: Tag of Component

