"""
4.5.1節のコードの説明
"""
from __future__ import annotations

# リスト4.14
class PhysicalDistributionBase:
    """
    物流拠点エンティティ

    Attributes: 略
    """
    def ship(self, baggage: Baggage) -> Baggage:
        """
        出庫

        Args:
            baggage (Baggage): 出庫する荷物
        
        Returns:
            Baggage: 出庫する荷物

        Note:
            実装はしません
        """
        pass

    def receive(self, baggage: Baggage):
        """
        入庫

        Args:
            baggage (Baggage): 受け取る荷物
        
        Returns: None

        Note:
            実装はしません
        """
        pass

    def transport(self, to: PhysicalDistributionBase, baggage: Baggage):
        """
        物流拠点に輸送のふるまいを定義する

        Args:
            to (PhysicalDistributionBase): 輸送先の物流拠点
            baggage: (Baggage): 輸送する荷物
        
        Returns: None

        Note:
            物流拠点が他の物流拠点に直接荷物を渡すことに違和感を覚える
            現実には配送の記録なども必要であり、それをここに書くのは違和感がある
        """
        shipped_baggage: Baggage = self.ship(baggage)
        to.receive(shipped_baggage)

        # たとえば配送の記録は必要だろうか